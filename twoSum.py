class Solution:
    def proverka(nums: list[int], target: int) -> bool:
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

    def type_validation(nums, target) -> bool:
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

    def twoSum(nums: list[int], target: int):
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

    def parse_inputlist(inp: str) -> list:
        result = list()
        inp = inp.split('[')
        inp = inp.split(']')
        inp = inp.split(',')
        for each in inp:
            try:
                num = int(each)
                result.append(num)
            except:
                continue

        return result

if __name__ == '__main__':
    # nums = [4, 5, 34, 2, 77645, 345, 789, 45787, 3323, 23, 4, 56, 7, 8, 9, 3, 2]
    # target = int(6)
    nums = Solution.parse_inputlist(input())
    target = int(input())

    if Solution.proverka(nums, target) and Solution.type_validation(nums, target):
        result = Solution.twoSum(nums, target)

    else:
        print('Proverka ne proydena')


    print(result)
