# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort to enable two-pointer technique and easy duplicate detection
        nums.sort()
        triplets = []

        # Fix first element, use two pointers for remaining two
        # -2 because we need space for left and r pointers
        for i in range(len(nums) - 2):
            # Skip duplicates for first element (compare with previous since sorted)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            r = len(nums) - 1

            while left < r:
                three_sum = nums[i] + nums[left] + nums[r]

                if three_sum == 0:
                    triplets.append([nums[i], nums[left], nums[r]])

                    # Skip all duplicate values for left pointer
                    while left < r and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip all duplicate values for r pointer
                    while left < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Move both pointers inward to find next potential triplet
                    left += 1
                    r -= 1

                elif three_sum < 0:
                    # Sum too small, move left pointer right to increase sum
                    left += 1

                elif three_sum > 0:
                    # Sum too large, move right pointer left to decrease sum
                    r -= 1

        return triplets
