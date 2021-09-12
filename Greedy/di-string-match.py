'''
problem

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it.
If there are multiple valid permutations perm, return any of them.
'''


class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        i, d = 0, len(s)
        perm = []
        for v in s:
            if v == 'I':
                perm.append(i)
                i += 1
            else:
                perm.append(d)
                d -= 1
        return perm + [i]
