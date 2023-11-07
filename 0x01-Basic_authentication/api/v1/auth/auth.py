#!/usr/bin/env python3
"""Authorization Class"""
from flask import Flask, request
from typing import TypeVar, List


class Auth:
    """Class to implement authorization"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method to handle authorization
        Returns:
          - False - path and excluded_paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Public method to handle authorization"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method to handle authorization"""
        return None
