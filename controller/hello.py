# -*- coding: utf-8 -*-
__author__ = 'liuxuebo'

import json
from flask import jsonify
from flask.ext.restful import Resource


class Hello(Resource):
    def get(self):
        return jsonify({})
