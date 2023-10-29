"""Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 """


class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(nums)[::-1]
        for i in range(len(arr) - 2):
            if arr[i] < arr[i + 1] + arr[i + 2]:
                return arr[i] + arr[i + 1] + arr[i + 2]
        return 0


sl = Solution()
sl.largestPerimeter
