class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = len(nums)
        while i < j and j != 1:
            if nums[i] == nums[i-1]:
                nums.pop(i-1)
                j -= 1
                continue
            i += 1




        return len(nums)

if __name__ == '__main__':
    Solution().removeDuplicates([1])
