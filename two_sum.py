'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

url:  https://leetcode.com/problems/two-sum/description/

'''


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        # extract the search and check if its present and return
        # and simply put new element with its location
        # can help with same no appear twice too
        for i, j in enumerate(nums):
            search = target - j
            if search in index_map:
                return [index_map[search], i]
            index_map[j] = i  # store after checking
