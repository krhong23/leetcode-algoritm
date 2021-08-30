'''
problem

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            if nums.count(n) < 2:
                return n


class BitManipulationSolution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
