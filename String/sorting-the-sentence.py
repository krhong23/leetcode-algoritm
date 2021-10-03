'''
problem

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
'''


class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = s.split(' ')
        hash_table = {}
        for a in array:
            print(a, a[-1], a[0:-1])
            hash_table[a[-1]] = a[0:-1]

        sorted_table = sorted(hash_table.items(), key=lambda item: item[0])

        result = ''
        for k, v in sorted_table:
            result += v + ' '

        return result.strip()
