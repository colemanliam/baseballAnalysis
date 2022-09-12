from flask import Flask, jsonify
from Baseball_data_api_backend import test
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

#creating the app
app = Flask(__name__)

test = {'playerid': "a"}

#creating engine for the DB
engine = create_engine('sqlite:///baseball_stats.db')


#setting up the automap of the DB
Base = automap_base()
Base.prepare(engine, reflect = True)

@app.route('/')
def index():
    return "voila"

@app.route('/Batters', methods=['GET'])
def get():
    return jsonify({'Batters': test})

if __name__ == "__main__":
    app.run(debug=True)