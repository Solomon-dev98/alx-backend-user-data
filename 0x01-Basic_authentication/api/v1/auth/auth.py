#!/usr/bin/env python3
# api/v1/auth/auth.py
"""An implementation of a class to manage the API authentication."""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class that manages the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ a public method that determines if authentication is required
        for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of excluded path.

        Returns:
            bool: false(for now, authentication will be done later).
            bool: True if path is None.
            bool: True if excluded_paths is None or empty.
            bool: False if path is in excluded_paths
            bool: False if excluded_paths contains /api/v1/status/
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        # Normalize the path (remove trailing slashes)
        path = path.rstrip('/')

        # check if the path is in excluded_path
        for excluded_path in excluded_paths:
            if excluded_path.rstrip('/') == path:
                return False
        # if none of the conditions match, return True
        return True

    def authorization_header(self, request=None) -> str:
        """ public method: retrieves authorization header.

        ArgS:
            request: The flask request obj.

        Return:
            str: None
        """
        if request is None:
            return None
        # check if Authorization header is not present, return None
        if 'Authorization' not in request.headers:
            return None

        # return the value of the 'Authorization' header
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on request.

        Args:
            request: The flask request object.

        Returns:
            TypeVar('User'): None
        """

        return None
