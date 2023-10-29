"""At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise."""
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five=five - 1
                ten =ten + 1
            elif ten > 0:
                five=five - 1
                ten =ten - 1
            else:
                five -= 3
            if five < 0:
                return False
        return True
sl=Solution()
sl.lemonadeChange