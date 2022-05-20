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
        # return true if path is None
        # excluded_paths is None or empty
        excluded_paths_len = len(excluded_paths)
        if path is None or excluded_paths is None or excluded_paths_len == 0:
            return True

        if path.endswith('/') and path in excluded_paths:
            return False
        else:
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
