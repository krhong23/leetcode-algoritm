# problem: Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i < length:
            if arr[i] == 0:
                for j in range(length - 1, i, -1):
                    arr[j] = arr[j - 1]
                i += 1
            i += 1
