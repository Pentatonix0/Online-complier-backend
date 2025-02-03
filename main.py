from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from compile import compile_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, origins="http://localhost:3000")

    api = Api(app, doc='/docs')
    api.add_namespace(compile_ns)

    return app
