class Solution:
    # def __init__(self):
    #     """
    #     LeetCode send all input only in first stdin.
    #     Probably like a two string with
    #     """
    #     super().__init__()
    #     # self._listnums = True
    #     # self._targetnum = True
    #     # While isinstance(self._listnums, bool) and isinstance(self._targetnum, bool):
    #     self._listnums = self._input_pr(input('please input list of numbers'))
    #     self._targetnum = self._input_pr(input('please input target num'))

    def _proverka(self, nums: list[int], target: int) -> bool:
        ans1 = True
        ans2 = True

        if 2 <= len(nums) <= 10 ** 4 and -10 ** 9 <= target <= 10 ** 9:
            ans1 = True
        else:
            ans1 = False

        for num in nums:
            if -10 ** 9 <= num <= 10 ** 9:
                ans2 = True
            else:
                ans2 = False

        if ans1 == False or ans2 == False:
            return False
        else:
            return True

    def _type_validation(self, nums, target) -> bool:
        ans1 = True
        ans2 = True

        for num in nums:
            if isinstance(num, int) == False:
                ans1 = False

        if isinstance(target, int) == False:
            ans2 = False

        if ans1 == False or ans2 == False:
            return False
        else:
            return True

    def _worker(self, nums: list[int], target: int):
        work_dict = {index: num for index, num in enumerate(nums)}
        result = None
        for index, num in work_dict.items():
            search_num = target - num
            for index2, num2 in work_dict.items():
                if index2 <= index:
                    continue

                if num2 == search_num:
                    result = [index, index2]
                    break
            if result != None:
                break

        return result

    def twoSum(self, nums: list[int], target: int, *args, **kwargs) -> str:
        """
        bound method,
        нужно возвращать уже готовый результат под выполнение в ЛитКод
        """
        # self._listnums = self._input_pr()
        # self._targetnum = self._input_pr()
        self._listnums = nums
        self._targetnum = target

        if self._proverka(nums, target) and self._type_validation(nums, target):
            return self._worker(nums, target, *args, **kwargs)
        else:
            return 'inupt doesnt valid'



    def _input_pr(self):
        result = list()
        inp = input()
        if inp[0] == '[' and inp[-1] == ']':
            inp = inp[1:-1]

            inp = inp.split(',')
            for each in inp:
                # try:
                num = int(each)
                result.append(num)
            # except:
            #     continue
            return result

        else:
            return int(inp)

    def _output_pr(self, res: list) -> str:
        result = str()
        str_res_list = [str(num) for num in res]
        nums_str = ','.join(str_res_list)

        return '[' + nums_str + ']'


# if __name__ == '__main__':
#     #     # nums = [4, 5, 34, 2, 77645, 345, 789, 45787, 3323, 23, 4, 56, 7, 8, 9, 3, 2]
#     #     # target = int(6)
#     #     # nums = Solution.input_pr(input())
#     #     # target = int(input())
#
#     print(Solution().twoSum())

if __name__ == '__main__':
    nums = [4, 5, 34, 2, 77645, 345, 789, 45787, 3323, 23, 4, 56, 7, 8, 9, 3, 2]
    target = int(6)
    Solution().twoSum(nums, target)