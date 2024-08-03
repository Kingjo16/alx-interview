#!/usr/bin/python3
"""Module for validating UTF-8 encoding."""


def validUTF8(data):
    """Determines if a list of integers represents valid UTF-8 characters."""
    remaining_bytes = 0
    total_bytes = len(data)
    for ind in range(total_bytes):
        if remaining_bytes > 0:
            remaining_bytes -= 1
            continue
        if type(data[ind]) != int or data[ind] < 0 or data[ind] > 0x10ffff:
            return False
        elif data[ind] <= 0x7f:
            remaining_bytes = 0
        elif data[ind] & 0b11111000 == 0b11110000:
            # Handling 4-byte UTF-8 character
            required_length = 4
            if total_bytes - ind >= required_length:
                continuation_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[ind + 1: ind + required_length],
                ))
                if not all(continuation_bytes):
                    return False
                remaining_bytes = required_length - 1
            else:
                return False
        elif data[ind] & 0b11110000 == 0b11100000:
            # Handling 3-byte UTF-8 character
            required_length = 3
            if total_bytes - ind >= required_length:
                continuation_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[ind + 1: ind + required_length],
                ))
                if not all(continuation_bytes):
                    return False
                remaining_bytes = required_length - 1
            else:
                return False
        elif data[ind] & 0b11100000 == 0b11000000:
            # Handling 2-byte UTF-8 character
            required_length = 2
            if total_bytes - ind >= required_length:
                continuation_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[ind + 1: ind + required_length],
                ))
                if not all(continuation_bytes):
                    return False
                remaining_bytes = required_length - 1
            else:
                return False
        else:
            return False
    return True
