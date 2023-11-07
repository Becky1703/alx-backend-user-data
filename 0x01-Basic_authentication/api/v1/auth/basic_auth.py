#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth
import re
import base64


class BasicAuth(Auth):
    """class inherits from Auth"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Function to extract base64 header"""
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None
