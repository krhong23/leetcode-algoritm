'''
problem
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for n in nums:
            if n == val:
                count += 1

        for i in range(count):
            nums.remove(val)

        return len(nums)


class TwoPointerSolution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        first, last = 0, len(nums)
        while first < last:
            if nums[first] == val:
                nums[last - 1], nums[first] = nums[first], nums[last - 1]
                last -= 1
            else:
                first += 1
        return first
