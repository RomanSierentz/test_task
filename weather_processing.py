    """
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries

import pandas as pd
import numpy as np

# TODO Import the dataset 

path = r'./data/weather_dataset.data'

with open(path, "r") as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines[1:]]

lines = [x.split(" ") for x in lines]

for i in range(len(lines)):
    while('' in lines[i]):
        lines[i].remove('')

for i in range(1, len(lines)):
    for j in range(3, 15):
        if "," in lines[i][j]:
            lines[i][j] = lines[i][j].replace(",",".")

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index

data = pd.DataFrame(np.array(lines[1:], dtype=str), columns=lines[0])

data["datetime_index"] = "19" + data["Yr"] + "-" + data["Mo"] + "-" + data["Dy"]
data["datetime_index"] = pd.to_datetime(data["datetime_index"])
data = data.set_index('datetime_index').drop(["Yr", "Mo", "Dy"], axis=1)
data

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them

#data.info() # дізнаємось що дата має тип object а це нам не підходить
def to_float(string):
    if string.replace('.', '', 1).isdigit():
        return float(string)
    else:
        return None

for i in range(1, 13):
    data['loc' + str(i)] = data['loc' + str(i)].apply(lambda x : to_float(x))   # переводимо в тип float
data.agg(["max", "min"]) # бачимо що max в loc9 дуже велике, видалимо рядок з цим значенням
data = data[data["loc9"] < 1e16]
data.agg(["max", "min"])

# TODO Write a function in order to fix date (this relate only to the year info) and apply it

            # фіксити date не потрібно

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]

data.index # переконуємось, що тип datetime64[ns]

# TODO Compute how many values are missing for each location over the entire record

data.isnull().sum()

# TODO Compute how many non-missing values there are in total

data.notnull().sum().sum()

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times

data.sum().sum() / data.notnull().sum().sum()

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days

loc_stats = data.agg(['min', 'max', 'mean', 'std'])
loc_stats

# TODO Find the average windspeed in January for each location

data[data.index.month == 1].mean()

# TODO Downsample the record to a yearly frequency for each location

data.groupby(data.index.year).mean()

# TODO Downsample the record to a monthly frequency for each location

data.groupby(by=[data.index.year, data.index.month] ).mean()

# TODO Downsample the record to a weekly frequency for each location

data.groupby(by=[data.index.year, data.index.week] ).mean()

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks

data_week21 = data[data.index.week <= 21]
data_week21 = data_week21[data_week21.index.year == 1961]
data_week21['week'] = data_week21.index.week
data_week21


stat_df = pd.DataFrame()
stat_df['mean'] = data_week21.groupby('week').mean().mean(axis=1)
stat_df['min'] = data_week21.groupby('week').min().min(axis=1)
stat_df['max'] = data_week21.groupby('week').max().max(axis=1)
stat_df