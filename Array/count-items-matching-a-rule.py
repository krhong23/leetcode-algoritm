'''
problem

You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item.
You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
'''


class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        for i in items:
            if ruleKey == "type":
                if i[0] == ruleValue:
                    count += 1
            elif ruleKey == "color":
                if i[1] == ruleValue:
                    count += 1
            else:
                if i[2] == ruleValue:
                    count += 1
        return count
