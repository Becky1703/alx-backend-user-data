#!/usr/bin/env python3
"""User session module"""
from models.base import Base


class UserSession(Base):
    """User session class inherits from Base"""
    def __init__(self, *args: list, **kwargs: dict):
        """Initialization of the User session"""
        super().__init__(*kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
