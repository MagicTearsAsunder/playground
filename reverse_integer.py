"""
Given a 32-bit signed integer, reverse digits of an integer.
"""

def reverse(x):

    check_if_negative = False

    if x < 0:
        x = abs(x)
        check_if_negative = True

    x = str(x)

    new_string = ""

    if check_if_negative:
            new_string += "-"
    for i in range(len(x)-1, -1, -1):
        new_string += x[i]

    new_string = int(new_string)

    if (new_string <= -2147483648) or (new_string > (2147483647)):
        return 0

    return new_string
