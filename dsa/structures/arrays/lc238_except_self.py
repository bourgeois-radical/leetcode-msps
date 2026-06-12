"""
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class InitialSolution:
    """
    takes too much memory because of final_products, products_left2right etc.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # These checks are not necessary since we are promised to have length = at least 2
        # if not nums:
        #     return None
        # elif len(nums) == 1:
        #     return None

        # We first want to traverse from lefr to right
        # e.g. nums = [2, 3, 5, 6]: for nums[2] we want to have a product of num[0] * num[1], that will become
        # answer_left2right[2] = num[0] * num[1] -> so, we collect all the products before the i
        # we will do the same when we traverse over the array backwards
        products_left2right = []
        product = 1
        for i in range(len(nums)):
            if i == 0:
                product = 1
                products_left2right.append(product)
                continue  # because for num[1], the product should equal just num[0]
            product *= nums[i - 1]
            products_left2right.append(product)

        products_right2left = []
        for i in reversed(range(len(nums))):
            if i == (len(nums) - 1):
                product = 1
                products_right2left.append(product)
                continue
            product *= nums[i + 1]
            products_right2left.append(product)

        products_right2left = list(reversed(products_right2left))
        final_products = [
            left * right
            for left, right in zip(products_left2right, products_right2left)
        ]

        return final_products


"""
Fishki:
- Prefix/suffix decomposition: split "everything except i" into
  "everything before i" × "everything after i." Prefix = beginning
  of array up to a point, suffix = remaining portion to the end.
- Two sequential passes ≠ nested loops: O(n) + O(n) = O(n).
- Reuse output array for O(1) space: first pass prefix, second pass suffix in-place.
- Multiplicative identity (1) as running start at boundaries.
"""


class ImprovedSolution:
    """
    An improved solution
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr_product = 1
        products = []
        for i in range(len(nums)):
            products.append(curr_product)
            curr_product *= nums[i]

        curr_product = 1
        for i in reversed(range(len(nums))):
            products[i] = curr_product * products[i]
            curr_product *= nums[i]

        return products


if __name__ == "__main__":
    solution = ImprovedSolution()
    nums_1 = [1, 2, 3, 4]
    nums_2 = [-1, 1, 0, -3, 3]
    print(solution.productExceptSelf(nums=nums_1))
