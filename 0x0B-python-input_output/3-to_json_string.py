#!/usr/bin/python3
"""Defines a function that converts an object to a json string"""
import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
