'''
problem

You are given an integer array nums (0-indexed).
In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
An array of length 1 is trivially strictly increasing.
'''


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = nums[0]
        for i, v in enumerate(nums):
            if i == 0:
                pass
            elif minimum >= v:
                nums[i] = minimum + 1
                minimum = nums[i]
                print(nums, minimum)

        return sum(nums)
