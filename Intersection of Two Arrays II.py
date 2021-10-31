class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        smallest = str()
        startIntersection = list()


        if len(nums1) <=len(nums2):
            smallest = 'nums1'
            other = 'nums2'
        else:
            smallest = 'nums2'
            other = 'nums1'

        originList = list(eval(other))

        for digitSmallest in eval(smallest):
            try:
                startIntersection.append(eval(other).index(digitSmallest))
                eval(other)[startIntersection[-1]] = '_'
            except ValueError:
                continue

        startIntersection = [originList[x] for x in startIntersection]

        return startIntersection

if __name__ == '__main__':
    Solution().intersect([1,2,2,1], [2,2])