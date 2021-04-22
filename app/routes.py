"""
FlaskSports route File

This file will contain all of the main routes from the front end to hit
"""

from app import app
import sqlite3

@app.route('/')
@app.route('/index')
def root():
    # Placeholder user for any testing/developing with without adding a user system
    user = {'username': 'Jody'}

    # Proof of concept code showing that we can connect to the database, run a query, and return the results to a webpage
    # conn = sqlite3.connect('Data/bbstats.sqlite3')
    conn = sqlite3.connect('Data/NBAdata.sqlite3')

    c = conn.cursor()
    c.execute('SELECT * FROM stats')
    stuff = c.fetchall()
    print(stuff[0][1])
    print(type(stuff))
    print(type(stuff[0][1]))
    # results = []

    # for row in stuff:
    #     results.append(row)
    return stuff[0][1]


if __name__ == '__main__':
    pass