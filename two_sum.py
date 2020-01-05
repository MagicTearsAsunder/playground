"""
Given an array of integers, return indices of the
two numbers such that they add up to a specific target.
You may assume that each input would have exactly
one solution, and you may not use the same element twice.
"""

def twoSum(nums, target):
    dictionary = {}

    for i, item in enumerate(nums):
        if target - item in dictionary:
            return [dictionary[target - item], i]
        else:
            dictionary[item] = i

    return 0

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
