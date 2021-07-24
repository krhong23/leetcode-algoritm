'''
problem
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
'''


class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[nums[i]] for i in range(len(nums))]


class EuclideanAlgorithmSolution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        q = len(nums)
        for i, c in enumerate(nums):
            nums[i] += q * (nums[c] % q)
        for i, _ in enumerate(nums):
            nums[i] //= q
        return nums
