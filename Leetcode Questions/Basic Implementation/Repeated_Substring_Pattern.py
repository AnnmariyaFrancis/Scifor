"""Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together."""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
          if n % i == 0:
             sub = s[:i]
             times = n // i
             if sub * times == s:
                 return True
        return False
s=Solution()
s.repeatedSubstringPattern