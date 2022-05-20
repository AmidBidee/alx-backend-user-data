#!/usr/bin/env python3
"""
Auth class Module
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    An Authentication class to manage API autentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth method
        """
        if path is not None and excluded_paths is not None:
            if excluded_paths == 0:
                return True
            if path not in excluded_paths:
                return True
            if path.endswith('/') and path not in excluded_paths:
                return True
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user method
        """
        return None
