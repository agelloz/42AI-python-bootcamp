import pandas as pd
import sys
sys.path.append('../ex00')
from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        res = self.df.loc[self.df.City == location, 'Year'].unique()
        return res

    def where(self, date):
        res = self.df.loc[self.df.Year == date, 'City'].unique()
        return res

if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
