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
        """

        return False

    def authorization_header(self, request=None) -> str:
        """ public method: retrieves authorization header.

        ArgS:
            request: The flask request obj.

        Return:
            str: None
        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on request.

        Args:
            request: The flask request object.

        Returns:
            TypeVar('User'): None
        """

        return None
