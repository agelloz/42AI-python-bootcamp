import numpy as np
import pandas as pd
import sys
sys.path.append('../ex00')
from FileLoader import FileLoader

def howManyMedals(df, name):
    df['Medal'].replace('', np.nan, inplace=True)
    data = df.loc[df.Name == name, ['Year', 'Medal']]
    data.dropna(subset=['Medal'], inplace=True)
    res = {}
    for index, row in data.iterrows():
        if row['Year'] not in res.keys():
            res[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if row['Medal'] == 'Gold':
            res[row['Year']]['G'] += 1 
        elif row['Medal'] == 'Silver':
            res[row['Year']]['S'] += 1 
        elif row['Medal'] == 'Bronze':
            res[row['Year']]['B'] += 1 
    return res


if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')
    print(howManyMedals(data, 'Kjetil Andr Aamodt'))
