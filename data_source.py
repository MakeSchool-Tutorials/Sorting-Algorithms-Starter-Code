import csv, sys

class DataSource():
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.headers = None
        self.rows = []
        self.parse()

    def parse(self):
        with open(self.csv_file) as data_file:
            reader = csv.reader(data_file)
            self.headers = next(reader) # first row of CSV is the headers
            self.rows = [row for row in reader] # remaining rows are data rows

if __name__ == "__main__":
    file = sys.argv[1]
    ds = DataSource(file)
    print("Parsing {}...".format(file))
    print()
    print("Headers: {}".format(', '.join(ds.headers)))
    print("Row count: {}".format(len(ds.rows)))
