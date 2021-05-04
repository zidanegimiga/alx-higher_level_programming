#!/usr/bin/python3


def max_integer(my_list=[]):
    """Returns the biggest integer of a list"""
    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
