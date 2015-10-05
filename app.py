import os

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

title = "Sorting SF GOV Data"

@app.route("/")
def index():
    return render_template('index.html', title=title)

if __name__ == "__main__":
    app.run()
