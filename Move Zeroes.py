class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        countZero = nums.count(0)
        countThis = 0
        # for i in range(0, len(nums)):
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))

        while i < len(nums) and countThis != countZero:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                countThis += 1
            else:
                i += 1

if __name__ == '__main__':
    print(Solution().moveZeroes([0,0,1,3,12]))