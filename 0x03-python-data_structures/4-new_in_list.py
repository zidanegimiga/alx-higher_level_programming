#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Make a copy of a list and replace an element in a certain positon
       in the copy. Leaves the original list unmodified.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list[:]
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
