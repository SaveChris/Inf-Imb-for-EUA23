import numpy as np
import pandas as pd


from scipy.stats import pearsonr
from datetime import datetime
from f_plots import plot_eua

# Import data
df = pd.read_excel('Data/Dataset_EUA23.xlsx')

# Define the target variable (EUA)
eua = df['EUA']

# Define the date variable
date = df['Date']

# Remove the date column from the data for correlations
df_ = df.drop(df.columns[[0]], axis=1)

# Brexit event
br_date = datetime(2020,2,1)
br_value = 23.21

# Change of Phase 3 to Phase 4
ph_date = datetime(2021,1,1)
ph_value =  33.69

# Plot the EUA price with the custom function
plot_eua(date, eua, br_date, br_value, ph_date)