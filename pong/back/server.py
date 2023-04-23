from flask import Flask, jsonify, request
from utils import get_sorted_scores
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 
@app.route('/specific_score')
def specific_score():
    place_n = int(request.args.get('pn'))
    res = get_sorted_scores()[place_n-1]
    return jsonify(res)
 
@app.route('/scores')
def scores():
    return jsonify(get_sorted_scores())

if __name__ == '__main__':
    app.run()