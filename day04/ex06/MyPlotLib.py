import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys
sys.path.append('../ex00')
from FileLoader import FileLoader

class MyPlotLib:

    @staticmethod
    def histogram(data, features):
        features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        data[features].hist() 
        plt.show()

    @staticmethod
    def density(data, features):
        features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        data[features].plot.kde(alpha=0.5) 
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        pd.plotting.scatter_matrix(data[features], alpha=0.2)
        plt.show()

    @staticmethod
    def box_plot(data, features):
        features = [f for f in features if np.issubdtype(data[f].dtype, np.number)]
        data[features].plot.box()
        plt.show()

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../resources/athlete_events.csv')
    
    sample = pd.pivot_table(df, index='Year', values=['Medal', 'Team', 'Age', 'City'], 
            aggfunc={'Medal':'count', 'Team':'count', 'Age':np.mean, 'City':'first'})
    print(sample)
    
    mpl = MyPlotLib()

    mpl.histogram(sample, ['Age'])
    mpl.histogram(sample, ['Medal', 'City', 'Team'])

    mpl.density(sample, ['Age'])
    mpl.density(sample, ['Medal', 'City', 'Team'])
    
    mpl.pair_plot(sample, ['Age'])
    mpl.pair_plot(sample, ['Medal', 'City', 'Team'])

    mpl.box_plot(sample, ['Age'])
    mpl.box_plot(sample, ['Medal', 'City', 'Team'])
