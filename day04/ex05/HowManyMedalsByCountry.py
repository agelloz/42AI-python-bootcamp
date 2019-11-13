import numpy as np
import pandas as pd
from FileLoader import FileLoader

def howManyMedalsByCountry(df, country):
    df['Medal'].replace('', np.nan, inplace=True)
    data = df.loc[df.Team == country, ['Year', 'Medal', 'Team', 'Event']]
    data.dropna(subset=['Medal'], inplace=True)
    data = data.drop_duplicates()
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
    print(howManyMedalsByCountry(data, 'France'))
