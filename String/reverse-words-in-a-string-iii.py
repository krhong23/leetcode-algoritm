# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        s_array = s.split(' ')
        for i, s_item in enumerate(s_array):
            s_array[i] = s_item[::-1]
        return ' '.join(s_array)
