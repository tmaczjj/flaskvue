from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import os
import requests

static_folder = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())) + "\\dist\\static")
template_folder = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())) + "\\dist")
app = Flask(__name__,
            static_folder=static_folder,
            template_folder=template_folder)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


if __name__ == '__main__':
   app.run(debug=True)