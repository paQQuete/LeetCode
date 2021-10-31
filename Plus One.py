class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # razrDigit = 0
        # sum = digits[-1]+1
        # if len(digits) == 1 and sum >= 10:
        #     digits[-1] = sum % 10
        #     digits.insert(0, 1)
        #     sum = 0
        #
        #
        # if sum >= 10:
        #
        #     for i in range(len(digits)-1,-1,-1):
        #         innerSum = digits[i] + 1
        #         if innerSum >= 10 and i==0:
        #             digits[i] = innerSum % 10
        #             digits.insert(0, 1)
        #         elif innerSum >= 10:
        #             digits[i] = innerSum % 10
        #
        #
        #         else:
        #             digits[i] = innerSum
        #
        #
        # else:
        #     digits[-1] = sum
        #
        # return digits

        perenosChetchik = 0

        for i in range(len(digits)-1,-1,-1):


            sum = digits[i] + 1
            if sum >= 10:
                perenosChetchik = 1
                digits[i] = sum % 10
            else:
                digits[i] = sum
                perenosChetchik = 0
                break

            if i == 0 and perenosChetchik == 1:
                digits.insert(0, perenosChetchik)

        return digits


if __name__ == '__main__':
    print(Solution().plusOne([1,2,3]))



