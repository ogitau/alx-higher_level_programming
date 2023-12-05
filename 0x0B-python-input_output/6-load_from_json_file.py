#!/usr/bin/python3
""" My Module for converting from JSON to Python"""
import json


def load_from_json_file(filename):
    """ Load JSON into Python Object from a file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
