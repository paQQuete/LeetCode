class Roman(str):
    def __init__(self, romanstring=''):
        super().__init__()
        self.romanstr = romanstring

    def romanToInt(self) -> int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        decimalInt = int()
        i = 0
        watchRomanstr = self.romanstr

        while i != len(self.romanstr):
            try:

                if romanDict[self.romanstr[i]] < romanDict[self.romanstr[i + 1]]:
                    number = romanDict[self.romanstr[i+1]] - romanDict[self.romanstr[i]]
                    decimalInt += number
                    i += 2
                else:
                    number = int(romanDict[self.romanstr[i]])
                    decimalInt += number
                    i += 1

            except IndexError:  # end of string, this hook cuz in IF-ELSE we call literal in string by index+1
                number = int(romanDict[self.romanstr[i]])
                decimalInt += number
                return decimalInt

        return decimalInt


class Solution:
    def romanToInt(self, s: str) -> int:
        return Roman(s).romanToInt()


if __name__ == '__main__':
    print(Solution().romanToInt('IV'))
