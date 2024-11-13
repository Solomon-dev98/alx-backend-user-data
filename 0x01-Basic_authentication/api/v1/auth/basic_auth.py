#!/usr/bin/env python3
# api/v1/auth/basic_auth.py
"""Implementation for a class for BasicAuth"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
     self, base64_authorization_header: str) -> str:
        """A method that returns the decoded value of a Base64 string.

        Args:
            - base64_authorization_header (str): the string to be decoded.

        Returns:
            str: returns the decoded base64 string.
        """

        # check for if base64_authorization_header is None
        if base64_authorization_header is None:
            return None

        # check if base64_authorization_header is not a string.
        if not isinstance(base64_authorization_header, str):
            return None

        # check for if base64_authorization_header is not a valid Base64
        try:
            # Validate the base64 part by decoding
            decoded = base64.b64decode(
                base64_authorization_header).decode('utf-8')

            # Try to decode the byte string to UTF-8 and return it.
        except (base64.binascii.Error, UnicodeDecodeError):
            # if decoding fails, return None
            return None

        return decoded

    def extract_user_credentials(
     self, decoded_base64_authorization_header: str) -> (str, str):
        """A public method that returns the user email and password form the
            decoded base64 decoded value.

        Args:
            decoded_base64_authorization_header (str): 
            the base64 string to be decoded.

        Returns:
            NoneType: None, decoded_base64_authorization_header is None.
            NoneType: None, decoded_base64_authorization_header is not a string.
            NoneType: None, decoded_base64_authorization_header doesn't
                    contain :
            str: useremail and the user password separated by a colon.
        """

        # Check if decoded_base64_authorization_header is none or a string.
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Check if it contains :
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # split the decoded string into email and password at ":"
        user_email, user_password = decoded_base64_authorization_header.split(":", 1)

        # return the user_email and user_password
        return user_email, user_password
