'''
problem

Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of arr.
'''


class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        preSum = 0
        for i in range(len(arr)):
            if i % 2 == 0:
                for j in range(len(arr) - i):
                    preSum += sum(arr[j:j + i + 1])
        return preSum
