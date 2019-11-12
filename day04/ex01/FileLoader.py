import pandas as pd

class FileLoader:

    @staticmethod
    def load(path):
        data = pd.read_csv(path)
        print('Loading dataset of dimensions {} x {}'
                .format(data.shape[0], data.shape[1]))
        return data

    @staticmethod
    def display(df, n):
        if n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))

if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')
    fl.display(data, 12)
    fl.display(data, -5)
