import sys

class CsvReader():
    def __init__(self, file_name, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file = open(file_name, 'r')
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.csv_lines = []
        self.data = []
        self.corrupted = self.parse_csv()

    def parse_csv(self):
        self.csv_lines = [line for line in self.file]
        row_count = len(self.csv_lines)
        col_count = len(self.csv_lines[0].split(self.sep))
        if self.header:
            self.data.append(self.csv_lines[0])
            self.csv_lines.pop(0)
        self.csv_lines = self.csv_lines[self.skip_top:]
        last_line = row_count - self.skip_bottom
        for i, l in enumerate(self.csv_lines):
            line = [e.strip() for e in filter(lambda x: x != '\n', l.split(self.sep))]
            if len(line) != col_count:
                return True
            self.data.append(line)
            if i == last_line:
                break
        return False

    def getdata(self):
        return self.data

    def getheader(self):
        if self.header is True:
            return self.data[0]

    def __enter__(self):
        if self.corrupted is True:
            return None
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()


if __name__ == "__main__":
    sys.argv.pop(0)
    if not len(sys.argv):
        exit()
    with CsvReader(sys.argv[0], skip_top=1) as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)
