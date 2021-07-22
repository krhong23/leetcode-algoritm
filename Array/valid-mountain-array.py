# problem: Given an array of integers arr, return true if and only if it is a valid mountain array.

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        top = False
        for i in range(1, len(arr) - 1):
            if arr[i - 1] >= arr[i] <= arr[i + 1]:
                return False
            if arr[i - 1] < arr[i] > arr[i + 1]:
                top = True

        return top
