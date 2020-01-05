"""
Determine whether an integer is a palindrome. An integer is a
palindrome when it reads the same backward as forward.
"""

def isPalindrome(x):

    n = str(x)

    reversed_n = ""

    for i in range((len(n)-1), -1, -1):
        reversed_n += n[i]

    if n == reversed_n:
        return True

    return False
