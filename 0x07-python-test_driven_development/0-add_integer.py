#!/usr/bin/python3
"""Addition module to add two integers
checks if 'a' is an integer or a float
checks if 'b' is an integer or a float

Return a + b"""


def add_integer(a, b=98):
    
    """Return a + b"""

    if not isinstance(a, (int, float)):

        """checks if 'a' is an integer or a float"""

        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        
        """checks if 'b' is an integer or a float"""
        
        raise TypeError("b must be an integer")
    return int(a) + int(b)

