import csv

class CsvReader():
    def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

def getdata():
    pass

def getheader()
    pass

if __name__ == "__main__":
    with Csvreader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
    with Csvreader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
