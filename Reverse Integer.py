class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        y = list()
        for each in x:
            y.append(each)

        underZero = False
        if y[0] == '-':
            underZero = True
            y.pop(0)

        y.reverse()

        output = int()
        i = 1

        while i != len(y)+1:
            output += int(y[-i]) * (10**(i-1))
            i += 1

        if underZero:
            output = output-(output*2)

        # 32bit check

        if -2**31 < output < (2**31)-1:
            return output
        else:
            return 0


if __name__ == '__main__':
    print(Solution().reverse(-123))