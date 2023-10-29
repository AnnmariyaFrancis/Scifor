"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 """
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            print("false")
        else:
            dict1 = {}
            dict2 = {}

            for char in s:
               if char not in dict1:
                  dict1[char] = 1
               else:
                  dict1[char] += 1

            for char in t:
                if char not in dict2:
                    dict2[char] = 1
                else:
                   dict2[char] += 1
            if dict1 == dict2:
                return True
            else:
                return Fale
s1=Solution()
s1.isAnagram