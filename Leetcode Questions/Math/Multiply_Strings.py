"""Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string."""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        first_number=int(num1)
        second_number=int(num2)
        product=first_number*second_number
        return str(product)
sl=Solution()
sl.multiply