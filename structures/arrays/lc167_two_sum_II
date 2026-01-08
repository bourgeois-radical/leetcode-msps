# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        l = 0
        r = len(numbers) - 1

        while l<r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            elif curr_sum == target:
                return [l+1, r+1]
            
        raise AssertionError("Guys, you promised that: 'The tests are generated such that there is exactly one solution.'")

'''
Fishka: Use left and right pointers. The left pointer increases the sum (when shifted to the right) 
and the right pointer decreases the sum (when shifted to the left) until a solution has been found.
'''