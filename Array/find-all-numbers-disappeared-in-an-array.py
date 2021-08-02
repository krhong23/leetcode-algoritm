# problem: Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.


class TimeLimitExceededSolution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            if i + 1 not in nums:
                arr.append(i + 1)
        return arr


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
