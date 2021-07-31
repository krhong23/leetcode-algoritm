# problem: Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNums = [float("-inf"), float("-inf"), float("-inf")]
        for num in nums:
            if num == maxNums[0] or num == maxNums[1] or num == maxNums[2]:
                continue
            elif num > maxNums[0]:
                maxNums[2], maxNums[1], maxNums[0] = maxNums[1], maxNums[0], num
                continue
            elif num > maxNums[1]:
                maxNums[2], maxNums[1] = maxNums[1], num
                continue
            elif num > maxNums[2]:
                maxNums[2] = num
                continue
        return maxNums[0] if maxNums[2] == float("-inf") else maxNums[2]
