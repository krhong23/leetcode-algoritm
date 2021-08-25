'''
problem

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
'''


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = [0] * len(nums)
        sumnums = 0
        for i, num in enumerate(nums):
            sumnums += num
            runningSum[i] = sumnums
        return runningSum
          
