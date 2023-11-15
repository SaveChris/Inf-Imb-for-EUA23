## Summary
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
