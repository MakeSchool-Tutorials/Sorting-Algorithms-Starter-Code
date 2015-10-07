import os
import csv

from flask import Flask
from flask import render_template, request

from data_sets import all as data_sets
from sort import timed_sort

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route("/")
def index():
    return render_template('index.html', title='')

@app.route("/<data_set_name>")
def data_view(data_set_name):
    data = data_sets[data_set_name]
    rows = data.rows
    row_count = len(rows)
    ex_time = 'N/A'
    sort_by = None

    if 'sort_by' in request.args:
        sort_by = request.args['sort_by']
        col_idx = data.headers.index(sort_by)
        rows, ex_time = timed_sort(rows, key=lambda r: r[col_idx])

    return render_template('table_view.html',
                           title=data.name,
                           headers=data.headers,
                           rows=rows,
                           row_count=row_count,
                           sortings=data.sortings,
                           sort_by=sort_by,
                           ex_time=ex_time)

if __name__ == "__main__":
    app.run()
