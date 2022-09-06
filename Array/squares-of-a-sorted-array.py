# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

import collections


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        for n in nums:
            array.append(n * n)
        array.sort()
        return array


class DequeSolution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = collections.deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)


class AnotherSolution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        array = [0] * length
        for i in range(0, length):
            array[i] = nums[i] * nums[i]
            i += 1
        array.sort()
        return array