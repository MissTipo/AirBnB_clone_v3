#!/usr/bin/python3
"""Endpoint (route) will be to return the status of API"""
from api.v1.views import app_views
from flask import *

@app_views.route('/status', strict_slashes=False)
def status():
    """Returns a JSON of a string"""
    return jsonify({"status":"OK"})
