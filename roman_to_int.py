"""
Given a roman numeral, convert it to an integer.
"""

def romanToInt(s):

    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    len_input = len(s)-1

    total_number = 0

    check = False

    for i in range(len_input):
        if dict[s[i]] < dict[s[i+1]]:
            total_number += dict[s[i+1]] - dict[s[i]]
            check = True
            continue
        if check:
            check = False
            continue

        total_number += dict[s[i]]

    if not check:
        total_number += dict[s[len_input]]

    return total_number
