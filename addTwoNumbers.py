# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def reversalLinkedList(cascadeList):
        current = cascadeList
        prev = None
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    @staticmethod
    def extractValues(cascadeList) -> int:
        extrValue = str()
        current = cascadeList
        while current is not None:
            extrValue += str(current.val)
            current = current.next

        return int(extrValue)





    # @staticmethod
    # def searchHead(node) -> bool:
    #
    @staticmethod
    def addTwoNumbers(l1, l2):
        return l1, l2


if __name__ == '__main__':
    l1, l2 = Solution.addTwoNumbers(l1=ListNode(val=2, next=
                                    ListNode(val=4, next=
                                             ListNode(val=3))),
                           l2=ListNode(val=5, next=
                                    ListNode(val=6, next=
                                             ListNode(val=4))))


    l1reverse = Solution.reversalLinkedList(l1)
    l2reverse = Solution.reversalLinkedList(l2)

    l1revExtr = Solution.extractValues(l1reverse)
    l2revExtr = Solution.extractValues(l2reverse)

    rawSum = list(reversed(str(l1revExtr + l2revExtr)))
    output = list()
    for symbol in rawSum:
        output.append(symbol)

    print(output)

