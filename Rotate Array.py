class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # srez = nums[-1:len(nums)-k-1:-1]
        # nums = nums[0:len(nums)-k]
        #
        # for digit in srez:
        #     nums.insert(0, digit)

        for i in range(k):
            nums.insert(0, nums.pop(-1))

if __name__ == '__main__':
    Solution().rotate([1,2,3,4,5,6,7], 3)