#!/usr/bin/env python3
"""Authentication template module
"""

from flask import request
from typing import List, Pattern, TypeVar
import os


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """requires authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = True if path[l_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """this function add authorization header"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """this method gets the current user"""
        None

    def session_cookie(self, request=None):
        """this function returns cookie value from a request
        """
        if request is None:
            return None
        _my_session_id = os.getenv("SESSION_NAME")
        return request.cookies.get(_my_session_id)
