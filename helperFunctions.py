"""
    This module will provide the helper functions which permit accessing the DB to provide the player information to the normal calls
"""

from sqlite3 import OperationalError
from sqlalchemy.orm import Session
from sqlalchemy import text, select


def getPlayerID (fName, lName, engine, Base):

    #creating a session
    with Session(engine) as session:
        People = Base.classes.People
        
        #handling query error
        try:
            result = session.execute(
                select(People.playerID, People.birthYear).
                where(People.nameLast == lName).
                where(People.nameFirst == fName).
                order_by(People.birthYear.desc())
            )
            
            return result.first()[0]
        except OperationalError:
            return None


if __name__ == "__main__":
    #testing imports
    import sqlalchemy as db
    from sqlalchemy.ext.automap import automap_base

    engine = db.create_engine('sqlite:///baseball_stats.db')

    
    #setting up the automap of the DB
    Base = automap_base()
    Base.prepare(autoload_with=engine, reflect = True)
    People = Base.classes.People

    #acutal tests
    print (getPlayerID("Jose", "Bautista", engine, Base))
    engine.dispose()
