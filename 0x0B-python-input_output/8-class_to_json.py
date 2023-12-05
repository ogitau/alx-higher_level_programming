#!/usr/bin/python3
""" My Module for converting objects into representation for JSON"""


def class_to_json(obj):
    """ Turns an object into nice representation for JSON"""
    return obj.__dict__
