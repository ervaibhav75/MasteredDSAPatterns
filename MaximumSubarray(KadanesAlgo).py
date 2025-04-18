'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

url : https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        summed = 0

        if len(nums) == 1:
            return nums[0]

        for i in nums:
            summed = summed + i
            maximum = max(maximum, i, summed)
            if summed < 0:
                summed = 0

        return maximum
