"""
Given an array nums of n integers,
are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""

def threeSum(nums):
    if not nums or len(nums) < 3:
        return []

    solution = []
    nums.sort()

    if not nums:
        return solution

    len_nums = len(nums) - 1
    for i in range(len_nums):
        j, k = i + 1, len_nums

        while j < k:
            the_sum = nums[i] + nums[j] + nums[k]

            if the_sum < 0:
                j += 1

            elif the_sum > 0:
                k -= 1

            else:
                new_solution = [nums[i], nums[j], nums[k]]

                if not new_solution in solution:
                    solution.append(new_solution)

                k -= 1
                j += 1

    return solution
