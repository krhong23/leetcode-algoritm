'''
problem

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it in the maximum amount of balanced strings.
Return the maximum amount of split balanced strings.
'''


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = result = 0
        for v in s:
            if v == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                result += 1

        return result