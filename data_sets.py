from csv_parser import parse

class DataSet:
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def load(self):
        data = parse(self.file)
        self.headers = data['headers']
        self.rows = data['rows']
        return self

# Load and export all data sets
bp = DataSet('Bike Parking', 'data/Bicycle_Parking__Public_.csv')
bp.sortings = ['Street Name', 'Location Name', 'Spaces', 'Racks']
bp.load()

sr = DataSet('Salary Ranges', 'data/Salary_Ranges_by_Job_Classification.csv')
sr.sortings = ['Biweekly High Rate', 'Biweekly Low Rate', 'Union Code']
sr.load()

ca = DataSet('Civic Art', 'data/SF_Civic_Art_Collection.csv')
ca.sortings = ['Artist', 'Location Description', 'Medium', 'Title']
ca.load()

all = {
    'bike_parking': bp,
    'salary_ranges': sr,
    'civic_art': ca
}
