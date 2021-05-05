import numpy as np
import pandas as pd

filepath = "Produktionsdaten.xlsx"

# load spreadsheet as a dict of DataFrame
# setting sheet_name=None loads all sheets, not just the first one
data = pd.read_excel(filepath, sheet_name=None)
print(data)

# get the data just for 2017.
# The 3 DataFrames are called "2017", "2018", and "2019".
data_2017 = data["2017"]
print(data_2017)

# create a DataFrame containing only the rows where Profilwert is 0
only_rows_with_zero = data_2017[data_2017["Profilwert"] == 0]
print(only_rows_with_zero)

# get the number of rows where Profilwert is 0 (in 2017)
number_of_zeroes = len(only_rows_with_zero)
print(number_of_zeroes)
