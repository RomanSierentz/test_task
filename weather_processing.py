"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""

# TODO Import the necessary libraries
import pandas as pd
import numpy as np
from datetime import datetime
# TODO Import the dataset 

path = r'./data/weather_dataset.data'
types = {'Yr': np.object_, 'Mo': np.object_, 'Dy': np.object_, 'loc1': np.object_,
         'loc2': np.object_, 'loc3': np.object_, 'loc4': np.object_, 'loc5': np.object_,
         'loc6': np.object_, 'loc7': np.object_, 'loc8': np.object_, 'loc9': np.object_,
         'loc10': np.object_, 'loc11': np.object_, 'loc12': np.object_}

locations = ['loc1', 'loc2', 'loc3', 'loc4', 'loc5', 'loc6', 'loc7', 'loc8', 'loc9', 'loc10', 'loc11', 'loc12']
data = pd.read_table(path, skiprows=1, delim_whitespace=True, dtype=types)

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data = data.rename(columns={'Yr': 'year', 'Mo': 'month', 'Dy': 'day'})
print('DATETIME NAMES')
print(data)


# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
def check_strange_data(data):
    data = data.stack().str.replace(',', '.').unstack()
    for loc in data.columns.values.tolist():
        data[loc] = pd.to_numeric(data[loc], errors='coerce')
        data = data.drop(data[getattr(data, loc) > 200].index)
    return data


data = check_strange_data(data)
print('DATA CLEANING')
print(data)


# TODO Write a function in order to fix date (this relate only to the year info) and apply it
def fix_year():
    data.year += 1900
    print('YEAR FIX')
    print(data)
fix_year()


# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
data['date'] = pd.to_datetime(data[['year', 'month', 'day']])
print(data.dtypes)

# TODO Compute how many values are missing for each location over the entire record
print('NAN IN EVERY COLUMN')
print(data.isna().sum())
# TODO Compute how many non-missing values there are in total
print('SUM OF NON NAN')
print(data.count().sum())

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
df2 = data[list(locations)]
mean = df2.mean(axis=1).mean()
print('MEAN')
print(mean)


# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
min_vals = ['min'] + data[list(locations)].min().values.tolist()
max_vals = ['max'] + data[list(locations)].max().values.tolist()
mean_vals = ['mean'] + data[list(locations)].mean().values.tolist()
std_vals = ['std'] + data[list(locations)].std().values.tolist()
loc_stats = pd.DataFrame(columns=['char']+locations)
loc_stats.loc[len(loc_stats)] = min_vals
loc_stats.loc[len(loc_stats)] = max_vals
loc_stats.loc[len(loc_stats)] = mean_vals
loc_stats.loc[len(loc_stats)] = std_vals
print('LOC_STATS')
print(loc_stats)


# TODO Find the average windspeed in January for each location
jan_stat = data[data['month'] == 1].mean()[list(locations)]
print('AVG FOR JANS')
print(jan_stat)

# TODO Downsample the record to a yearly frequency for each location
yearly = data.groupby(pd.PeriodIndex(data['date'], freq="Y"))[locations].mean()
print('YEARLY')
print(yearly)

# TODO Downsample the record to a monthly frequency for each location
monthly = data.groupby(pd.PeriodIndex(data['date'], freq="M"))[locations].mean()
print('MONTHLY')
print(monthly)

# TODO Downsample the record to a weekly frequency for each location
weekly = data.groupby(pd.PeriodIndex(data['date'], freq="W"))[locations].mean()
print('WEEKLY')
print(weekly)


# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
weeks21_min = data.groupby(data.date.dt.isocalendar().week)[locations].min().head(21)
weeks21_max = data.groupby(data.date.dt.isocalendar().week)[locations].max().head(21)
weeks21_mean = data.groupby(data.date.dt.isocalendar().week)[locations].mean().head(21)
weeks21_std = data.groupby(data.date.dt.isocalendar().week)[locations].std().head(21)
print(f'Min for 21 weeks: {weeks21_min}')
print(f'Max for 21 weeks: {weeks21_max}')
print(f'Mean for 21 weeks: {weeks21_mean}')
print(f'Std for 21 weeks: {weeks21_std}')
