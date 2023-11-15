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

# Plotting Correlations Phase 3 and 4
def plot_corr(correlations_3, correlations_4):
    """
    Plots the correlations for phase 3 and 4.

    Parameters:
    correlations_3 (pandas.DataFrame): The correlation data for phase 3.
    correlations_4 (pandas.DataFrame): The correlation data for phase 4.

    Returns:
    fig (matplotlib.figure.Figure): The figure object.
    ax (matplotlib.axes.Axes): The axes object.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,4), dpi=700)
    
    correlations_3.plot(kind='bar', color='k', alpha=0.7, ax=ax1)
    ax1.bar(1, correlations_3[1], color='tab:cyan', alpha=0.7) # ERIX ind.
    ax1.bar(12, correlations_3[12], color='tab:olive', alpha=0.7) # Coal
    ax1.bar(24, correlations_3[24], color='tab:purple', alpha=0.7) # Nat. Gas
    ax1.bar(15, correlations_3[15], color='tab:red', alpha=0.7) # Unc. EUR/CHF
    ax1.bar(20, correlations_3[20], color='tab:blue', alpha=0.7) # EUR/CHF Spot
    ax1.get_xticklabels()[1].set_color('tab:cyan')
    ax1.get_xticklabels()[12].set_color('tab:olive')
    ax1.get_xticklabels()[24].set_color('tab:purple')
    ax1.get_xticklabels()[15].set_color('tab:red')
    ax1.get_xticklabels()[20].set_color('tab:blue')
    ax1.set_ylabel('Correlation Coefficient')
    ax1.grid(axis='both', color="black", alpha=.1)
    ax1.set_title('Correlations - Phase 3')
    
    correlations_4.plot(kind='bar', color='k', alpha=0.7, ax=ax2)
    ax2.bar(6, correlations_4[6], color='tab:cyan', alpha=0.7) # ERIX ind
    ax2.bar(17, correlations_4[17], color='tab:olive', alpha=0.7) # Coal
    ax2.bar(5, correlations_4[5], color='tab:purple', alpha=0.7) # Nat. Gas
    ax2.bar(14, correlations_4[14], color='tab:red', alpha=0.7) # Unc. EUR/CHF
    ax2.bar(4, correlations_4[4], color='tab:blue', alpha=0.7) # EUR/CHF Spot
    ax2.get_xticklabels()[6].set_color('tab:cyan')
    ax2.get_xticklabels()[17].set_color('tab:olive')
    ax2.get_xticklabels()[5].set_color('tab:purple')
    ax2.get_xticklabels()[14].set_color('tab:red')
    ax2.get_xticklabels()[4].set_color('tab:blue')
    ax2.set_ylabel('Correlation Coefficient')
    ax2.grid(axis='both', color="black", alpha=.1)
    ax2.set_title('Correlations - Phase 4')

    plt.savefig('../Figures/Fig_2_Correlations_3_4.png')
    return plt.show()