class Solution:
    def firstUniqChar(self, s: str) -> int:

        sList = list(s)

        for i in range(0, len(sList)):

            if sList.count(sList[i]) == 1:
                return i

            if i == len(sList)-1:
                return int(-1)

if __name__ == '__main__':
    print(Solution().firstUniqChar("leetcode"))