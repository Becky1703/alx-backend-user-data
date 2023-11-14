#!/usr/bin/env python3
"""User authentication"""
import bcrypt


from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Method hashes a password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
