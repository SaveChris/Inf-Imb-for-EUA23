import numpy as np
from dadapy._utils.metric_comparisons import _return_imbalance
from dadapy._utils.utils import compute_nn_distances
from dadapy import Data

def return_inf_imb_perturbed_d1_to_d2(d1: Data, d2: Data, k=1, n_perturbations=10, sigma=1e-7):
    """Return the information imbalalce from d1 to d2.

    Args:
        d1 (Data): The first dataset
        d2 (Data): The second dataset
        k (int, optional): The number of neighbours for the imbalance computations. Defaults to 1.
        n_perturbations (int, optional): The number of perturbations. Defaults to 100.

    Returns:
        mean and standard deviation of the imbalance estimates from d1 to d2.
    """
    imbalances_X1toX2 = []
    for i in range(n_perturbations):
        if sigma is None:
            X1_i = d1.X
            X2_i = d2.X
        else:
            X1_i = d1.X + np.random.normal(0, sigma, d1.X.shape)
            X2_i = d2.X + np.random.normal(0, sigma, d2.X.shape)
        _, d1_dist_indices = compute_nn_distances(
            X1_i, d1.maxk, d1.metric, d1.period
        )  
        _, d2_dist_indices = compute_nn_distances(
            X2_i, d2.maxk, d2.metric, d2.period
        )
        imb_X1toX2 = _return_imbalance(d1_dist_indices, d2_dist_indices, k=k)
        imbalances_X1toX2.append(imb_X1toX2)
    mean, std = np.mean(imbalances_X1toX2), np.std(imbalances_X1toX2)
    return mean, std