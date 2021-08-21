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


class SortSolution(object):
    def sortArrayByParity(self, A):
        A.sort(key=lambda x: x % 2)
        return A


class TwoPassSolution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])
