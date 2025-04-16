'''
Given a sorted array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i = 0 
        j = len(nums)-1
        while i <= j:
            if nums[i] + nums[j] > target:
                j = j-1 
            elif nums[i] + nums[j] < target:
                i = i + 1
            elif nums[i] + nums[j] == target:
                return [i,j]

        
