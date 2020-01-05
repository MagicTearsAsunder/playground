"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until
the first non-whitespace character is found. Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral
number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty or
it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
"""

def myAtoi(string):
    the_digit = ""
    found_the_digit = False

    for i in range(len(string)):
        if not string[i].isdigit() and found_the_digit:
            break
        if ((string[i] == "-" or string[i] == "+") and the_digit == "") or string[i].isdigit():
            the_digit += string[i]
            found_the_digit = True
        if the_digit == "" and string[i] != " ":
            return 0

    if the_digit == "" or the_digit == "-":
        return 0

    try:
        the_digit = int(the_digit)
    except ValueError:
        return 0

    if the_digit > 2147483647:
        return 2147483647
    elif the_digit < -2147483648:
        return -2147483648
    else:
        return the_digit
