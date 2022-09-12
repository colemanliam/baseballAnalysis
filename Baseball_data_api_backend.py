"""
    writing the backend functions which will query the sql db to create the views repsonsible and then package the data in a python dictionary to pass to the app for the app to provide
    the api calls
"""

#imports
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from helperFunctions import getPlayerID

#gets a single players stats
def sp_stats (playerFirstName = None, playerLastName = None, year = None, engine = None, conn = None, Base = None):
    
    #returning None if no DB engine or connnection is passed into the backend
    if engine is None or conn is None: return None

    #checking for valid player name if not returning empty dict
    if playerFirstName is None and playerLastName is None:
        return {}

    #using getPlayer id func to get the player ID from the DB
    playerID = getPlayerID(playerFirstName, playerLastName, engine, conn, Base)
    if playerID is None: return None

    #creating query to get player batting stats
    if year is None:
        query = f"SELECT * \
        FROM Batting \
        WHERE playerID LIKE '%{playerID}%' \
        ORDER BY yearID desc"
        result = conn.execute(text(query))
    elif True:
        pass


if __name__ == "__main__":
    engine = create_engine('sqlite:///baseball_stats.db')
    with engine.connect() as conn:
        pass
    engine.dispose()