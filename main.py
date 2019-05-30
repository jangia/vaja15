from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route('/')
def index():
    some_text = 'Message from handler!'
    current_year = datetime.datetime.now().year
    cities = ["Boston", "Ljubljana", "Dunaj", "Beograd"]
    logged_in = False
    return render_template('index.html', some_text=some_text, current_year=current_year, cities=cities, logged_in=logged_in)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(use_reloader=True)