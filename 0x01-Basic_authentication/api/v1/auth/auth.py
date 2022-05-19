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

        return False

    def authorization_header(self, request=None) -> TypeVar('User'):
        """
        authorization header method
        """
        return None
