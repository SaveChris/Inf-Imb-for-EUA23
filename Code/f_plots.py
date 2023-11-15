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
    try:
        fig, ax = plt.subplots(figsize=(8,4), dpi=700)
        ax.plot(date, eua, color ='black', label = 'EU ETS price')
        ax.plot(br_date, br_value, marker = "X", markersize = "13", markeredgecolor = "black", markerfacecolor="gold", label = 'Brexit')
        plt.axvline(x=ph_date, color='black', linestyle='--', label = 'Change of Phase')
        ax.fill_between(x=date, y1 = eua, where = (date >= datetime(2019,12,1)) & (date <= datetime(2022,2,23)), facecolor='royalblue', alpha=0.6, label = 'COVID-19 pandemic')
        ax.fill_between(x=date, y1 = eua, where = (date >= datetime(2022,2,24)) & (date <= datetime(2023,4,23)), facecolor='skyblue', alpha=0.6, label = 'Energy Crisis')
        ax.legend()
        ax.set_ylabel('Price', fontsize = 15)
        ax.set_xlabel('Time', fontsize = 15)
        plt.grid(axis='both',color="black", alpha=.1)
        plt.savefig('../Figures/Fig_1_EUA.png')
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")

# Plotting Correlations Phase 3
def plot_corr_3(correlations_3):
    """
    Plots the correlations for phase 3.

    Parameters:
    correlations_3 (pandas.DataFrame): The correlation data for phase 3.

    Returns:
    fig (matplotlib.figure.Figure): The figure object.
    ax (matplotlib.axes.Axes): The axes object.
    """
    fig, ax = plt.subplots(figsize=(4,4), dpi=700)
    correlations_3.plot(kind='bar', color='k', alpha=0.7, figsize=(8, 4))
    plt.bar(1, correlations_3[1], color='tab:cyan', alpha=0.7) # ERIX ind.
    plt.bar(12, correlations_3[12], color='tab:olive', alpha=0.7) # Coal
    plt.bar(24, correlations_3[24], color='tab:purple', alpha=0.7) # Nat. Gas
    plt.bar(15, correlations_3[15], color='tab:red', alpha=0.7) # Unc. EUR/CHF
    plt.bar(20, correlations_3[20], color='tab:blue', alpha=0.7) # EUR/CHF Spot
    plt.ylabel('Correlation Coefficient')
    plt.grid(axis='both', color="black", alpha=.1)
    plt.title('Correlations - Phase 3')

    ax.get_xticklabels()[1].set_color('tab:cyan')
    ax.get_xticklabels()[12].set_color('tab:olive')
    ax.get_xticklabels()[24].set_color('tab:purple')
    ax.get_xticklabels()[15].set_color('tab:red')
    ax.get_xticklabels()[20].set_color('tab:blue')
    plt.savefig('../Figures/Fig_2.1_Correlations_3.png')

    return plt.show() 

# Plotting Correlations Phase 4
def plot_corr_4(correlations_4):
    """
    Plots the correlations for phase 4.

    Parameters:
    correlations_4 (pandas.DataFrame): The correlation data for phase 3.

    Returns:
    fig (matplotlib.figure.Figure): The figure object.
    ax (matplotlib.axes.Axes): The axes object.
    """
    fig, ax = plt.subplots(figsize=(4,4), dpi=700)
    correlations_4.plot(kind='bar', color='k', alpha=0.7, figsize=(8, 4))
    plt.bar(6, correlations_4[6], color='tab:cyan', alpha=0.7) # ERIX ind.
    plt.bar(17, correlations_4[17], color='tab:olive', alpha=0.7) # Coal
    plt.bar(5, correlations_4[5], color='tab:purple', alpha=0.7) # Nat. Gas
    plt.bar(14, correlations_4[14], color='tab:red', alpha=0.7) # Unc. EUR/CHF
    plt.bar(4, correlations_4[4], color='tab:blue', alpha=0.7) # EUR/CHF Spot
    plt.ylabel('Correlation Coefficient')
    plt.grid(axis='both', color="black", alpha=.1)
    plt.title('Correlations - Phase 4')
    ax = plt.gca()
    ax.get_xticklabels()[6].set_color('tab:cyan')
    ax.get_xticklabels()[17].set_color('tab:olive')
    ax.get_xticklabels()[5].set_color('tab:purple')
    ax.get_xticklabels()[14].set_color('tab:red')
    ax.get_xticklabels()[4].set_color('tab:blue')
    plt.savefig('../Figures/Fig_2.2_Correlations_4.png')
    return plt.show()