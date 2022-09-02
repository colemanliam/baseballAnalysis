"""
    This module will provide the helper functions which permit accessing the DB to provide the player information to the normal calls
"""
a= "A"
print(a)
"""
from sqlalchemy import text


def getPlayerID (fName, lName, engine, conn):
    query = "SELECT playerID, birthYear \
        FROM People \
        WHERE nameLast LIKE '%" + lName + "%' AND nameFirst LIKE '%" + fName+"%' \
        ORDER BY birthYear desc"
    result = conn.execute(db.text(query))

    return result


if __name__ == "__main__":
    #testing imports
    import sqlalchemy as db
    engine = db.create_engine('sqlite:///baseball_stats.db')
    conn = engine.connect()
    

    print (getPlayerID("Jose", "Bautista", engine, conn))
    conn.close()
    engine.dispose()
"""