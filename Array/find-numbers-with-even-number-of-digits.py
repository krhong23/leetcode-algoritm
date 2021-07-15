# problem: Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution():
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            digit = 1
            while n / 10 <> 0:
                n = n / 10
                digit += 1
            print(n, digit, digit % 2)
            if digit % 2 == 0:
                count += 1
        return count
