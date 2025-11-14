# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_map = {}

        for curr_index, curr_num in enumerate(nums):
            looked_for = target - curr_num
            if looked_for in value_index_map:
                return [value_index_map[looked_for], curr_index]
            else:
                value_index_map[curr_num] = curr_index
            
'''
Fishka: Use a hash map as a look-up to optimize time complexity from O(n^2) to O(n) at cost of additional memory.
'''