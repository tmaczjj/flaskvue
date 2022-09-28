from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import os

static_folder = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())) + "\\dist\\static")
template_folder = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())) + "\\dist")
app = Flask(__name__,
            static_folder=static_folder,
            template_folder=template_folder)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


if __name__ == '__main__':
   app.run(debug=True)