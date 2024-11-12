#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)

# CORS setup
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize auth variable
auth = None

# check if AUTH_TYPE is set in environment variables
# and load the appropriate authentication class
if os.getenv("AUTH_TYPE"):
    auth_type = os.getenv("AUTH_TYPE")

    # use BasicAuth if AUTH_TYPE is equal basic_auth
    if auth_type == "basic_auth":
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()

    # use Auth if AUTH_TYPE is equal to auth
    if auth_type == "auth":
        from api.v1.auth.auth import Auth
        auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Request unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden error handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """Filter requests before they are processed"""
    if auth is None:
        return
    # list of exempt paths
    exempt_paths = ['/api/v1/status/',
                    '/api/v1/unauthorized/',
                    '/api/v1/forbidden/']

    # if the request path is not in the exempt list, check authentication
    if request.path not in exempt_paths:

        # check if authentication is required for the current path
        if auth.require_auth(request.path, exempt_paths):

            # if the authorization is required for the current path
            if auth.authorization_header(request) is None:
                abort(401)  # Unauthorized

            # if no current user is found, abort with 403
            if auth.current_user(request) is None:
                abort(403)  # Forbidden


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
