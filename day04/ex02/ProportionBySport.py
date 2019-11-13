import pandas as pd
from FileLoader import FileLoader

def proportionBySport(df, year, sport, gender):
    frac = len(df.loc[(df.Year == year) & (df.Sport == sport) & (df.Sex == gender), 'Name'].unique())
    total = len(df.loc[(df.Year == year) & (df.Sex == gender), 'Name'].unique())
    return frac / total

if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')
    print(proportionBySport(data, 2004, 'Tennis', 'F'))
