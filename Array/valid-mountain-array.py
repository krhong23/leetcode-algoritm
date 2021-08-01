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


class OnePassSolution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        length = len(arr)
        i = 0

        while i + 1 < length and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == length - 1:
            return False

        while i + 1 < length and arr[i] > arr[i + 1]:
            i += 1

        return i == length - 1
