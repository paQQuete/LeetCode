class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for digit in nums:
            if nums.count(digit) == 1:
                return digit


