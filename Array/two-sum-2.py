# 167. Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# case2. Using two pointer, but Time Limit Exceeded
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while (l <= r):
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif r == len(numbers) - 1:
                l += 1
                r = l + 1
            else:
                r += 1


# case2. Using two pointer
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while (l <= r):
            twosum = numbers[l] + numbers[r]
            if twosum == target:
                return [l + 1, r + 1]
            elif twosum < target:
                l += 1
            else:
                r -= 1
