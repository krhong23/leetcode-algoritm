'''
problem

You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
'''


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        dictionary = {}
        count = 0
        for i, word in enumerate(words):
            result = True
            for w in word:
                if w not in allowed:
                    result = False
            dictionary[word, i] = result

        for k, v in dictionary.items():
            print(k, v, allowed)
            if v is True:
                count += 1

        return count
