import pandas as pd
from FileLoader import FileLoader

def proportionBySport(df, year, sport, gender):
    res = 0.0

    return res

if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')
    print(proportionBySport(data, 2004, 'Tennis', 'F'))
