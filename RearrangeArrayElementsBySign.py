
'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

url: https://leetcode.com/problems/rearrange-array-elements-by-sign/
video: https://www.youtube.com/watch?v=h4aBagy4Uok
'''
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        #initiating both counters below so that we can increment them by 2
        pos_counter = 0
        neg_counter  = 1
        output = [-1 ] * len(nums)
        for i in nums:
            if i > 0:
                output[pos_counter] = i
                pos_counter += 2
            else:
                output[neg_counter] = i
                neg_counter += 2
        
        return output
