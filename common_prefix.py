"""
Write a function to find the longest common prefix
string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs):

    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    length_of_strings = []

    for i in range(len(strs)):
        length_of_strings.append(len(strs[i]))

    common_prefix = ""

    for j in range(min(length_of_strings)):
        for k in range(len(strs)-1):
            if strs[k][j] == strs[k+1][j]:
                if k == len(strs)-2:
                    common_prefix += strs[k][j]
                continue
            else:
                return common_prefix

    return common_prefix
