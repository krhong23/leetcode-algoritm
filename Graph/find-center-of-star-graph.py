'''
problem

There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi.
Return the center of the given star graph.
'''
from collections import defaultdict


class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        dictionary = defaultdict(int)
        for edge in edges:
            for e in edge:
                dictionary[e] += 1

        return max(dictionary, key=dictionary.get)
