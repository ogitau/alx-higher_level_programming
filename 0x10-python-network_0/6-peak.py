#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """func to pic a list of integers"""

    size =len(list_of_integers)
    mid_elmt = size
    mid_idx = size // 2

    if size == 0:
        return None

    while True:
        mid_elmt = mid_elmt // 2
        if (mid_idx < size - 1 and
                list_of_integers[mid_idx] < list_of_integers[mid_idx + 1]):
            if mid_elmt // 2 == 0:
                mid_elmt = 2
            mid_idx = mid_idx + mid_elmt // 2
        elif mid_elmt > 0 and list_of_integers[mid_idx]\
                < list_of_integers[mid_idx - 1]:
            if mid_elmt // 2 == 0:
                mid_elmt = 2
            mid_idx = mid_idx - mid_elmt // 2
        else:
            return list_of_integers[mid_idx]
