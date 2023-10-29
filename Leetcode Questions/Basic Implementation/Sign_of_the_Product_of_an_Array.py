"""There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product)."""

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product=1
        for i in nums:
            product=product*i
        if product>0:
              return 1
        elif product==0:
              return 0
        else:
              return -1
a=Solution()
a.arraySign