#!/usr/bin/python3
"""function that convert JSON string to obj"""
import json


def from_json_string(my_str):
    """returns obj represented as aJSON string"""
    return json.loads(my_str)
