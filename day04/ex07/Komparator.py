import sys
sys.path.append('../ex06')
from MyPlotLib import MyPlotLib
from FileLoader import FileLoader
import seaborn as sns
from matplotlib import pyplot as plt

class Komparator:
    def __init__(self, df):
        self.data = df
    
    def compare_box_plots(self, categorical_var, numerical_var):
        df = self.data[[categorical_var, numerical_var]].dropna()
        meds = df.groupby(categorical_var).median()
        smeds = meds[numerical_var].sort_values(ascending=False)
        sns.boxplot(y=categorical_var, x=numerical_var, data=df, order=smeds.index, orient='h') 
        plt.show()

    def density(self, categorical_var, numerical_var):
        pass

    def compare_histograms(self, categorical_var, numerical_var):
        pass

if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')

    kp = Komparator(data)
    kp.compare_box_plots('Sport', 'Weight')
