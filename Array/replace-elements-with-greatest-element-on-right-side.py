'''
problem
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.
'''


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        count = 1
        length = len(arr)
        while count < length:
            arr[count - 1] = max(arr[count:])
            count += 1
        arr[-1] = -1
        return arr
