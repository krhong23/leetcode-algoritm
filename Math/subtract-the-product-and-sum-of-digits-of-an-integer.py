'''
problem

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        productNum = 1
        sumNum = 0
        while n > 0:
            productNum *= n % 10
            sumNum += n % 10
            n /= 10

        return productNum - sumNum
