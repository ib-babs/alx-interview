#!/usr/bin/python3
'''UTF-8 Validation'''


def validUTF8(data):
    '''Validates data as per UTF-8'''
    if not data or all(type(datum) != int for datum in data):
        return False

    for datum in data:
        byte = datum & 0xFF
        if byte > 127:
            return False
    return True
