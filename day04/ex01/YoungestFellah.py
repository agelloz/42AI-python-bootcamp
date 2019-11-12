import numpy as np
from FileLoader import FileLoader

def youngestFellah(df, year):
    men = np.min(df.loc[lambda x: x.Sex == 'M', ['Age', 'Year']]
            .loc[lambda x: x.Year == year, 'Age'])
    women = np.min(df.loc[lambda x: x.Sex == 'F', ['Age', 'Year']]
            .loc[lambda x: x.Year == year, 'Age'])
    return {'f': women, 'm': men}

if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')
    print(youngestFellah(data, 2004))
