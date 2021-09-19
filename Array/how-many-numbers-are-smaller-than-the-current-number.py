'''
problem

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_table = {}

        for i, n in enumerate(sorted(nums)):
            if n not in hash_table:
                hash_table[n] = i
        return [hash_table[n] for n in nums]
