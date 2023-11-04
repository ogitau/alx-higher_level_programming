#!/usr/bin/env python3
def no_c(my_string):
    oth = []
    for x in my_string:
        if x != 'c' and x != 'C':
            oth.append(x)
    return "".join(oth)
