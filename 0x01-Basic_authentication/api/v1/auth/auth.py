#!/usr/bin/env python3
"""Authorization Class"""
from flask import Flask, request
from typing import TypeVar, List
import re


class Auth:
    """Class to implement authorization"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method to handle authorization
        Returns:
          - False - path and excluded_paths
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = ''
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Public method to handle authorization"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method to handle authorization"""
        return None
