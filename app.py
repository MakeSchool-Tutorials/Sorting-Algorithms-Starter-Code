import os
import csv

from flask import Flask
from flask import render_template, request

from data_sets import all as data_sets

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route("/")
def index():
    return render_template('index.html', title=title)

@app.route("/<data_set_name>")
def data_view(data_set_name):
    data = data_sets[data_set_name]

    if 'sort_by' in request.args:
        col_idx = data.headers.index(request.args['sort_by'])
        rows = sorted(data.rows, key=lambda r: r[col_idx])
    else:
        rows = data.rows

    return render_template('table_view.html', title='Bike Parking', headers=data.headers, rows=rows, sortings=data.sortings)

if __name__ == "__main__":
    app.run()
