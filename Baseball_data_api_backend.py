"""
    writing the backend functions which will query the sql db to create the views repsonsible and then package the data in a python dictionary to pass to the app for the app to provide
    the api calls
"""

#imports
from sqlalchemy import create_engine

engine = create_engine('sqlite:///baseball_stats.db')
conn = engine.connect()

#gets a single players stats
def sp_stats (playerFirstName = None, playerLastName = None, year = None, engine = engine, conn = conn):
    pass