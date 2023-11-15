import matplotlib.pyplot as plt
from datetime import datetime

# Plotting EUA price
def plot_eua(date, eua, br_date, br_value, ph_date):
    """
    Plot the EU ETS price with additional events marked.

    Parameters:
    date (list): List of dates.
    eua (list): List of EU ETS prices.
    br_date (list): List of Brexit dates.
    br_value (list): List of Brexit values.
    ph_date (datetime): Date of change of phase.

    Returns:
    fig (matplotlib.figure.Figure): The figure object.
    """
    fig, ax = plt.subplots(figsize=(8,4), dpi=700)
    ax.plot(date, eua, color ='black', label = 'EU ETS price')
    ax.plot(br_date, br_value, marker = "X", markersize = "13", markeredgecolor = "black", markerfacecolor="gold", label = 'Brexit')
    ax.axvline(x=ph_date, color='black', linestyle='--', label = 'Change of Phase')
    ax.fill_between(x=date, y1 = eua, where = ((date >= datetime(2019,12,1)) & (date <= datetime(2022,2,23))) | ((date >= datetime(2022,2,24)) & (date <= datetime(2023,4,23))), facecolor='royalblue', alpha=0.6, label = 'COVID-19 pandemic')
    ax.legend()
    ax.set_ylabel('Price', fontsize = 15)
    ax.set_xlabel('Time', fontsize = 15)
    ax.grid(axis='both',color="black", alpha=.1)
    return fig

# Plotting Correlations Phase 3
def plot_corr_3(correlations_3):
    """
    Plot the correlations for phase 3.

    Parameters:
    correlations_3 (pandas.DataFrame): DataFrame containing the correlations.
    """

    fig, ax = plt.subplots(figsize=(8, 4), dpi=700)
    correlations_3.plot(kind='bar', color='black', alpha=0.7, ax=ax)
    
    colors = ['tab:cyan', 'tab:olive', 'tab:purple', 'tab:red', 'tab:blue']
    indices = [1, 12, 24, 15, 20]
    for i in range(len(indices)):
        ax.bar(indices[i], correlations_3[indices[i]], color=colors[i], alpha=0.7)
    
    ax.set_ylabel('Correlation Coefficient')
    ax.grid(axis='both', color="black", alpha=.1)
    ax.set_title('Correlations - Phase 3')
    
    color_indices = [1, 12, 24, 15, 20]
    color_names = ['tab:cyan', 'tab:olive', 'tab:purple', 'tab:red', 'tab:blue']
    for i in range(len(color_indices)):
        ax.get_xticklabels()[color_indices[i]].set_color(color_names[i])

# Plotting Correlations Phase 4
def plot_corr_4(correlations_4, figsize=(4, 4), dpi=700, title='Correlations - Phase 4', color_scheme=None):
    """
    Plots the correlations for phase 4.

    Parameters:
    correlations_4 (pandas.Series): The correlation coefficients for phase 4.
    figsize (tuple, optional): The size of the figure. Defaults to (4, 4).
    dpi (int, optional): The resolution of the figure. Defaults to 700.
    title (str, optional): The title of the plot. Defaults to 'Correlations - Phase 4'.
    color_scheme (list, optional): The color scheme for the bars. Defaults to None.

    Returns:
    tuple: The figure and axis objects.
    """
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    correlations_4.plot(kind='bar', color='black', alpha=0.7, ax=ax)
    
    if color_scheme is None:
        color_scheme = ['tab:cyan', 'tab:olive', 'tab:purple', 'tab:red', 'tab:blue']
    
    indices = [6, 17, 5, 14, 4]
    for i, index in enumerate(indices):
        ax.bar(index, correlations_4[index], color=color_scheme[i], alpha=0.7)
    
    ax.set_ylabel('Correlation Coefficient')
    ax.grid(axis='both', color="black", alpha=.1)
    ax.set_title('Correlations Phase 4')
    
    for i, index in enumerate(indices):
        ax.get_xticklabels()[index].set_color(color_scheme[i])
    
    return fig, ax
