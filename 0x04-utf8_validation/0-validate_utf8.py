#!/usr/bin/python3
"""
method that determines if a given data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    Args:
        data: the data set
    Returns:
        True if data is a valid UTF-8 encoding, else False
    """

    byte_count = 0

    for num in data:
        if byte_count == 0:
            # Check if the byte is a single-byte character (leading 0)
            if (num >> 7) == 0:
                byte_count = 0
            
            # Check if the byte is a 2-byte character (leading 110)
            elif (num >> 5) == 0b110:
                byte_count = 1
            
            # Check if the byte is a 3-byte character (leading 1110)
            elif (num >> 4) == 0b1110:
                byte_count = 2
            # Check if the byte is a 4-byte character (leading 11110)
            elif (num >> 3) == 0b11110:
                byte_count = 3
            else:
                # If none of the above conditions are met, it's an invalid byte
                return False
        else:
            # Check if the byte is a continuation byte (starts with 10)
            if (num >> 6) != 0b10:
                return False
            byte_count -= 1

    # Check if all bytes have been used
    return byte_count == 0
