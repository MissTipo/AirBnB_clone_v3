#!/usr/bin/python3
"""
Creates a new view for State objects that handles all
default RESTFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():

    """Retrieves the list of all"""
    states = storage.all(State)
    # return jsonify([state.to_dict() for state in states.values()])

    state_list = []
    for state in states.values():
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def state_object(state_id):
    """Retrieves a State object"""
    id_state = storage.get(State, state_id)
    if id_state is None:
        abort(404)

    return jsonify(id_state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    return jsonify({})
