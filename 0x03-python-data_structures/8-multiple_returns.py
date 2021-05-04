#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""
    length = len(sentence)
    if sentence:
        first = sentence[0]
    else:
        first = None
    return (length, first)
