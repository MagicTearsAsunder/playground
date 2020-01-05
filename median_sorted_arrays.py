"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""

def findMedianSortedArrays(nums1, nums2):
    merged_list = (nums1 + nums2)
    merged_list.sort()
    len_list = len(merged_list)
    if (len_list % 2) != 0:
        return float(merged_list[len_list//2])
    else:
        return float((merged_list[len_list//2] + merged_list[(len_list//2)-1])/2)
