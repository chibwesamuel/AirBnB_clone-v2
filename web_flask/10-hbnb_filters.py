#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template, jsonify
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Method to remove current SQLAlchemy Session after each request"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Route to display HTML page with filters"""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
