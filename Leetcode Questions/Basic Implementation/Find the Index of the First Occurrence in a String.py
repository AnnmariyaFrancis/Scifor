"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack"""

class Solution(object):
    def strStr(self, haystack, needle):
      k=len(needle)
      l=len(haystack)
      for i in range(l):
         if haystack[i:k+i] == needle:
            return i
            break
      else:
            return -1
c=Solution()
c.strStr