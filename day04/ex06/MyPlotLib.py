from FileLoader import FileLoader
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class MyPlotLib:

    @staticmethod
    def histogram(data, features):
        plt.plot() 
        pass

    @staticmethod
    def density(data, features):
        pass

    @staticmethod
    def pair_plot(data, features):
        pass

    @staticmethod
    def box_plot(data, features):
        pass

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../resources/athlete_events.csv')
    
    years = df['Year'].drop_duplicates().sort_values()
    print(repr(years))
    print(type(years))
    
    tennis_medals = df.loc[(df.Sport == 'Tennis') & (df.Medal != np.nan) , ['Year', 'Medal']].dropna()
    tennis_medals = tennis_medals.groupby('Year').size()
    print(repr(tennis_medals))
    print(type(tennis_medals))
    
    mpl = MyPlotLib()
    mpl.histogram(df, {'Years': years, 'Medals': tennis_medals})
