#!/usr/bin/python3
"""Endpoint (route) will be to return the status of Api"""
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import *


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.teardown_appcontext
def teardown(exception):
    """closes the current sqlalchemy session"""
    storage.close()

if __name__=="__main__":
    host = getenv('HBNB_API_HOST') or '0.0.0.0'
    port = getenv('HBNB_API_PORT') or '5000'
    app.run(host=host, port=port, threaded=True)
