"""An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise."""


class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 2: return True

        isdecreasing = False
        isincreasing = False
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                isincreasing = True
            elif nums[i - 1] < nums[i]:
                isdecreasing = True
            if isdecreasing and isincreasing:
                return False
        return True


sl = Solution()
sl.isMonotonic