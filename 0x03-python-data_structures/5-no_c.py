#!/usr/bin/python3


def no_c(my_string):
    """Removes all characters c and C from a string"""
    res = ''.join([my_string[i] for i in range(len(my_string))
                   if my_string[i] not in "cC"])
    return res
