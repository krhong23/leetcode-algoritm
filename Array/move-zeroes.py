# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# case1
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length, 0, -1):
            if nums[i - 1] == 0:
                for j in range(i, length):
                    nums[j - 1] = nums[j]
                nums[length - 1] = 0
                length -= 1
        return nums

# case2. Using two pointer
class TwoPointerSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t1, t2 = 0, len(nums) - 1
        while t1 <= t2:
            if nums[t1] == 0:
                nums.append(nums.pop(t1))
                t2 -= 1
                t1 -= 1
            t1 += 1