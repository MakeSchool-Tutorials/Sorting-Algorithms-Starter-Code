import csv, sys

def parse(file):
    parsed = {
        'headers': None,
        'rows': []
    }

    with open(file) as data_file:
        reader = csv.reader(data_file)
        parsed['headers'] = next(reader) # first row of CSV is the headers
        parsed['rows'] = [row for row in reader] # remaining rows are data rows

    return parsed

if __name__ == "__main__":
    file = sys.argv[1]
    data = parse(file)
    print("Parsing {}...".format(file))
    print()
    print("Headers: {}".format(', '.join(data['headers'])))
    print("Row count: {}".format(len(data['rows'])))
