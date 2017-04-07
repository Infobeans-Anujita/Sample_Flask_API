from flask import Flask,jsonify, request
import json

with open('apifile.json') as data_file:
    data = json.load(data_file)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'lets create wow'})


@app.route('/users', methods=['GET'])
def return_all():
    return jsonify(data['users'])


@app.route('/users/<id>', methods=['GET'])
def return_one(id):
    if id in data['users']:
        return jsonify(data['users'][id])
    else:
        print "no record found"


if __name__ == "__main__":
    app.run(debug=True, port=8081)
