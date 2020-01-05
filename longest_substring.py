"""
Given a string, find the length of the
longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):

    if s is "":
        return 0

    longest_substring = 1
    temporal_substring = ""

    for i in range(len(s)):

        if s[i] in temporal_substring:

            temporal_substring = temporal_substring.replace(temporal_substring[0], "")

            if longest_substring < len(temporal_substring):
                longest_substring = len(temporal_substring)

        temporal_substring += s[i]

    if len(temporal_substring) > longest_substring:
        return len(temporal_substring)
    else:
        return longest_substring
