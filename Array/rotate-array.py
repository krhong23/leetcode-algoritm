# 189. Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]