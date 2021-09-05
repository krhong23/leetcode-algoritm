'''
problem

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        result = 0
        hash_table = {jewel: 0 for jewel in jewels}
        for i, stone in enumerate(stones):
            if stone in hash_table:
                result += 1

        return result
