# -*- coding: utf-8 -*-

__author__ = 'liuxuebo'
version = '1.0'

from flask.ext.restful import Api
from flask import Flask
from controller import Hello

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, '/')

json_config = app.config.get('RESTFUL_JSON', dict())
json_config["encoding"] = 'utf8'
json_config["ensure_ascii"] = False

app.config.setdefault('RESTFUL_JSON', json_config)


def run_model():
    port = 8001
    host = '0.0.0.0'
    app.run(host=host, port=port)


if __name__ == '__main__':
    run_model()
