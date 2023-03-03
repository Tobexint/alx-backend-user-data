#!/usr/bin/env python3
"""
This module contains functions for encrypting password
and checking for valid passords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """this function takes a str argument(password) and encodes it returning a
    salted, hashed password which is  a byte string"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """  function that expects 2 arguments and returns a boolean.
    Arguments:
    hashed_password: bytes type
    password: string type

    Returns:
        True if valid(matches) or False if not matching
    """
    is_valid = False
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        is_valid = True
    return is_valid
