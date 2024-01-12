import numpy as np
from dadapy import Data

from scipy.stats import rankdata


def _get_conditional_ranks_d1_to_d2(d1: Data, d2: Data):
    """Return the conditional ranks from d1 to d2.

    Args:
        d1 (Data): The first dataset
        d2 (Data): The second dataset

    Returns:
        conditional_ranks: The conditional ranks from d1 to d2.
    """
    assert d1.dist_indices.shape[0] == d2.dist_indices.shape[0]
    N = d1.dist_indices.shape[0]

    to_remove = [np.where(d1.dist_indices[i, :] == i)[0][0] for i in range(N)]

    d1_dist_indices = np.array([np.delete(d1.dist_indices[i, :], to_remove[i]) for i in range(N)])
    d1_distances = np.array([np.delete(d1.distances[i, :], to_remove[i]) for i in range(N)])

    conditional_ranks = []

    for i in range(N):
        _, counts = np.unique(d1_distances[i, :], return_counts=True)
        k_neigh = d1_dist_indices[i, :counts[0]]
        wr = [np.where(idx == d2.dist_indices[i, :])[0][0] for idx in k_neigh]
        conditional_ranks.append(wr)

    return conditional_ranks


def _get_average_conditional_ranks_d1_to_d2(d1: Data, d2_matrix: np.ndarray):
    """Return the average-tie conditional ranks from d1 to d2.

    Args:
        d1 (Data): The first dataset
        d2 (Data): The second dataset

    Returns:
        conditional_ranks: The conditional ranks from d1 to d2.
    """
    assert d1.dist_indices.shape[0] == d2_matrix.shape[0] == d2_matrix.shape[1]
    N = d1.dist_indices.shape[0]

    # remove self-distances form distances and dist indices
    to_remove = [np.where(d1.dist_indices[i, :] == i)[0][0] for i in range(N)]
    d1_dist_indices = np.array([np.delete(d1.dist_indices[i, :], to_remove[i]) for i in range(N)])
    d1_distances = np.array([np.delete(d1.distances[i, :], to_remove[i]) for i in range(N)])

    conditional_ranks = []

    # assign np.inf to the diagonal of d2_matrix to exclude self-distances
    np.fill_diagonal(d2_matrix, np.inf)

    for i in range(N):
        # get the indices of the all first nearest neighbours
        _, counts = np.unique(d1_distances[i, :], return_counts=True)
        k_neigh = d1_dist_indices[i, :counts[0]]

        d2_rank = rankdata(d2_matrix[i, :], method="average")
        
        wr = [d2_rank[idx] for idx in k_neigh]
        conditional_ranks.append(wr)

    return conditional_ranks


def _get_average_imbalance_from_d1_to_d2(d1: Data, d2_matrix: np.ndarray):
    conditional_ranks = _get_average_conditional_ranks_d1_to_d2(d1, d2_matrix)
    N = d1.dist_indices.shape[0]

    # compute total number of elements in conditional ranks
    total_elements = sum([len(ranks) for ranks in conditional_ranks])

    # compute sum of conditional ranks
    sum_conditional_ranks = sum([sum(ranks) for ranks in conditional_ranks])

    # compute imbalance
    imbalance = sum_conditional_ranks / total_elements * 2.0 / N

    return imbalance

def _get_imbalance_from_d1_to_d2(d1: Data, d2: Data):
    conditional_ranks = _get_conditional_ranks_d1_to_d2(d1, d2)
    N = d1.dist_indices.shape[0]

    # compute total number of elements in conditional ranks
    total_elements = sum([len(ranks) for ranks in conditional_ranks])

    # compute sum of conditional ranks
    sum_conditional_ranks = sum([sum(ranks) for ranks in conditional_ranks])

    # compute imbalance
    imbalance = sum_conditional_ranks / total_elements * 2.0 / N

    return imbalance