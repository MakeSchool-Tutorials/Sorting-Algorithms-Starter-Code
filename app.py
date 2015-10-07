import os
import csv

from flask import Flask
from flask import render_template, request

from data_source import DataSource

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route("/")
def index():
    return render_template('index.html', title=title)

@app.route("/bike_parking")
def bike_parking():
    bp = DataSource('data/Bicycle_Parking__Public_.csv')
    sortings = ['Street Name', 'Location Name', 'Spaces', 'Racks']

    if 'sort_by' in request.args:
        col_idx = bp.headers.index(request.args['sort_by'])
        rows = sorted(bp.rows, key=lambda r: r[col_idx])
    else:
        rows = bp.rows

    return render_template('table_view.html', title='Bike Parking', headers=bp.headers, rows=rows, sortings=sortings)

@app.route("/salary_ranges")
def salary_ranges():
    bp = DataSource('data/Salary_Ranges_by_Job_Classification.csv')
    sortings = ['Biweekly High Rate', 'Biweekly Low Rate', 'Union Code']

    if 'sort_by' in request.args:
        col_idx = bp.headers.index(request.args['sort_by'])
        rows = sorted(bp.rows, key=lambda r: r[col_idx])
    else:
        rows = bp.rows

    return render_template('table_view.html', title='Salary Ranges', headers=bp.headers, rows=rows, sortings=sortings)

@app.route("/civic_art")
def civic_art():
    bp = DataSource('data/SF_Civic_Art_Collection.csv')
    sortings = ['Artist','Geometry','Location Description','Medium','Title']

    if 'sort_by' in request.args:
        col_idx = bp.headers.index(request.args['sort_by'])
        rows = sorted(bp.rows, key=lambda r: r[col_idx])
    else:
        rows = bp.rows

    return render_template('table_view.html', title='Civic Art', headers=bp.headers, rows=rows, sortings=sortings)

if __name__ == "__main__":
    app.run()
