# problem: Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution():
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxCount = 0

        for i in nums:
            if i == 1:
                count += 1
                if maxCount < count:
                    maxCount = count
            else:
                count = 0
        return maxCount


class SimpleSolution():
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 0
        return max(count, maxCount)
