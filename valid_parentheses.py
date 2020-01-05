"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

def isValid(s):
    if not s:
        return True
    if len(s)%2 != 0:
        return False

    the_list = []
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    dictionary = {"}": "{", "]": "[", ")": "("}

    if s[0] in closing:
        return False

    for item in s:

        if item in opening:
            the_list.append(item)

        elif item in closing:
            current_len = len(the_list)-1
            if dictionary[item] == the_list[current_len]:
                the_list.pop(current_len)
            else:
                return False

        else:
            return False

    if not the_list:
        return True
    else:
        return False
