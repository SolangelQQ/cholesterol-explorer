from flask import Flask
from flask_cors import CORS
from adapter.api import init_api
from adapter.dash_app import init_dash

def create_app():
    app = Flask(__name__)
    CORS(app)
    init_api(app)
    init_dash(app)
    return app
