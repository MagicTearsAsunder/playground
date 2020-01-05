"""
Given a sorted array and a target value, return the index
if the target is found. If not, return the index where it would
be if it were inserted in order.
You may assume no duplicates in the array.
"""


def searchinsert(nums: list, target: int) -> int:
    if not nums:
        return None
    if target in nums:
        return nums.index(target)
    if target > nums[len(nums)-1]:
        return len(nums)
    if target < nums[0]:
        return 0

    i = 0
    j = len(nums) - 1
    while j != i:
        index = (j + i) // 2

        if nums[index] < target and nums[index+1] > target:
            return index + 1

        if nums[index] > target:
            j = index
        else:
            i = index + 1

    return -1


nums = [1,3,5,6]
target = 5
print(searchinsert(nums, target))
