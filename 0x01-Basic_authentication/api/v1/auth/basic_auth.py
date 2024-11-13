#!/usr/bin/env python3
# api/v1/auth/basic_auth.py
"""Implementation for a class for BasicAuth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth"""

    def extract_base64_authorization_header(
     self, authorization_header: str) -> str:
        """A method that extracts Base64 part of the Authorization_header.

        Args:
            - authorization_header (str): authorization request.

        Returns:
            NoneType: None, authorization_header is None.
            NoneType: None, authorization_header is not a string.
            NoneType: None, authorization header doesn't start with basic.
            str: string
        """
        # check for if authorization is None.
        if authorization_header is None:
            return None

        # check for if authorization is not a string.
        if not isinstance(authorization_header, str):
            return None

        # check for if authorization_header doesn't start by Basic
        if not authorization_header.startswith("Basic "):
            return None

        # Return the part after "Basic "
        return authorization_header[6:]  # skip "Basic " (6 chars)
