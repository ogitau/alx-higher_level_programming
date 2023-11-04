#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= 4:
        cpylist = my_list.copy()
        return cpylist
    del my_list[idx]
    cpylist = my_list.copy()
    return cpylist
