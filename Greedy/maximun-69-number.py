'''
problem

Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
'''


class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = list(str(num))
        for i, v in enumerate(temp):
            if v == '6':
                temp[i] = '9'
                break

        return "".join(temp)
