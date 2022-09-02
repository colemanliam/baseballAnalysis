from flask import Flask, jsonify
from Baseball_data_api_backend import test

app = Flask(__name__)

test = {'playerid': "a"}

@app.route('/')
def index():
    return "voila"

@app.route('/Batters', methods=['GET'])
def get():
    return jsonify({'Batters': test})

if __name__ == "__main__":
    app.run(debug=True)