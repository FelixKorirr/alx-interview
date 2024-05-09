#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Determine if a given dataset represents utf8."""
    n, m1, m2 = 0, 1 << 7, 1 << 6

    for num in data:
        mask = 1 << 7
        if n == 0:
            while mask & num:
                n += 1
                mask = mask >> 1
            if n == 0:
                continue
            if n == 1 or n > 4:
                return False
        else:
            if not (num & m1 and not (num & m2)):
                return False
        n -= 1
    return n == 0
