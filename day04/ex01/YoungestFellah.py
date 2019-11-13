import numpy as np
from FileLoader import FileLoader

def youngestFellah(df, year):
    men = np.min(df.loc[(df.Sex == 'M') & (df.Year == year), 'Age'])
    women = np.min(df.loc[(df.Sex == 'F') & (df.Year == year), 'Age'])
    return {'f': women, 'm': men}

if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')
    print(youngestFellah(data, 2004))
