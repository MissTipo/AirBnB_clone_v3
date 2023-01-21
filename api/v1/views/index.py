from api.v1.views import app_views
from flask import *

@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status":"OK"})
