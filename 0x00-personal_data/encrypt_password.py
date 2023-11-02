#!/usr/bin/env python3
"""Password Encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Function to hash a password using a random salt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Function checks is a hashed password was formed from the given
    password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
