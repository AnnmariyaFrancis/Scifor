
"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string."""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=""
        l1 = len(word1)
        l2 = len(word2)
        l = max(l1,l2)
        for i in range(l):
            if i < l1:
                merged += word1[i]
            if i < l2:
                merged += word2[i]
        return merged
s1=Solution()
s1.mergeAlternately