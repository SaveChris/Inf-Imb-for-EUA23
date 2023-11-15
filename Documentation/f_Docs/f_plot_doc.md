## Summary - *plot_eua*
This code defines a function called `plot_eua` that plots the EU ETS price with additional events marked on the graph.

## Example Usage
```python
date = [datetime(2019, 1, 1), datetime(2019, 1, 2), datetime(2019, 1, 3)]
eua = [10, 15, 12]
br_date = [datetime(2019, 1, 2)]
br_value = [15]
ph_date = datetime(2019, 1, 2)
plot_eua(date, eua, br_date, br_value, ph_date)
```
This code will plot the EU ETS price with the given dates and prices. It will also mark the Brexit date and the change of phase date on the graph.

## Code Analysis
### Inputs
- `date` (list): A list of dates.
- `eua` (list): A list of EU ETS prices.
- `br_date` (list): A list of Brexit dates.
- `br_value` (list): A list of Brexit values.
- `ph_date` (datetime): The date of change of phase.
___
### Flow
1. Create a figure and axes for the plot.
2. Plot the EU ETS prices using the `date` and `eua` lists.
3. Plot the Brexit dates and values as markers on the graph.
4. Plot a vertical line at the change of phase date.
5. Fill the area between the EU ETS prices and the x-axis with a color for the COVID-19 pandemic period.
6. Fill the area between the EU ETS prices and the x-axis with a color for the energy crisis period.
7. Add a legend to the graph.
8. Set the y-axis label to "Price" and the x-axis label to "Time".
9. Show the plot.
___
### Outputs
- `fig` (matplotlib.figure.Figure): The figure object representing the plot.
___

***

## Summary - *plot_corr*
This code defines a function called `plot_corr` that plots correlation data for two different phases. It uses the `matplotlib` library to create a figure with two subplots, each representing the correlation data for a specific phase. The function takes two pandas DataFrames as input, which contain the correlation data for phase 3 and phase 4 respectively. The function then plots the correlation data using bar charts, with different colors for specific variables of interest. The resulting figure is saved as a PNG file and displayed.

## Example Usage
```python
correlations_3 = pd.DataFrame(...)
correlations_4 = pd.DataFrame(...)
plot_corr(correlations_3, correlations_4)
```

## Code Analysis
### Inputs
- `correlations_3` (pandas DataFrame): The correlation data for phase 3.
- `correlations_4` (pandas DataFrame): The correlation data for phase 4.
___
### Flow
1. Create a figure object and two axes objects using `plt.subplots()`.
2. Plot the correlation data for phase 3 on the first subplot using `correlations_3.plot()`.
3. Add additional bars to the phase 3 plot for specific variables of interest using `ax1.bar()`.
4. Customize the appearance of the phase 3 plot, such as setting colors and labels.
5. Plot the correlation data for phase 4 on the second subplot using `correlations_4.plot()`.
6. Add additional bars to the phase 4 plot for specific variables of interest using `ax2.bar()`.
7. Customize the appearance of the phase 4 plot, such as setting colors and labels.
8. Save the figure as a PNG file and display it using `plt.savefig()` and `plt.show()`.
___
### Outputs
- `fig` (matplotlib.figure.Figure): The figure object representing the plotted correlations.
- `ax` (matplotlib.axes.Axes): The axes object representing the subplots.
___


***