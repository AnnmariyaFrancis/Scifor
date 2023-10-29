"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only."""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        length=0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            length += 1
        return length
s1=Solution()
s1.lengthOfLastWord