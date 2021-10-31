class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for each in nums:
            if nums.count(each) > 1:
                return True

        return False

if __name__ == '__main__':
    Solution().containsDuplicate([2,14,18,22,22])