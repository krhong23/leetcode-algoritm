# problem: Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        beg, end = 0, len(nums) - 1

        while beg <= end:
            if nums[beg] % 2 == 0:
                beg += 1
            else:
                nums[beg], nums[end] = nums[end], nums[beg]
                end -= 1
        return nums
