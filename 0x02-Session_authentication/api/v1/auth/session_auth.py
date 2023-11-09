#!/usr/bin/env python3
"""Session Authentication"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User
from flask import request


class SessionAuth(Auth):
    """Class inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Function creates a session id for the user"""
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Function returns a user id based on a session id"""
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> str:
        """Function retrieves the user associated with the request"""
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)