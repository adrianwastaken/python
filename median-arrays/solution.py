# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = heapq.merge(nums1,nums2)
        final = list(final)
        if len(final)%2 != 0:
            return final[len(final)//2]
        else:
            left = int(len(final)/2) - 1
            right = int(len(final)/2)
            return (final[left]+final[right])/2
