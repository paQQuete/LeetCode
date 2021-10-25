import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reversalLinkedList(self, cascadeList):
        current = cascadeList
        prev = None
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    def extractValues(self, cascadeList) -> int:
        extrValue = str()
        current = cascadeList
        while current is not None:
            extrValue += str(current.val)
            current = current.next

        return int(extrValue)

    def unpackSolution(self, sum: int) -> list:
        return sum.split('')

    def input_parse(self, inp_string):
        inp_string = inp_string.replace('{', '(')
        inp_string = inp_string.replace('}', ')')
        inp_string = inp_string.replace(': ', '=')
        inp_string = inp_string.replace(', ', ',')
        # inp_list = inp_string.split()

        return inp_string

    def addTwoNumbers(self, l1, l2):

        # l1 = eval(self.input_parse(l1))
        # l2 = eval(self.input_parse(l2))

        l1reverse = self.reversalLinkedList(l1)
        l2reverse = self.reversalLinkedList(l2)

        l1revExtr = self.extractValues(l1reverse)
        l2revExtr = self.extractValues(l2reverse)

        rawSum = l1revExtr + l2revExtr
        revertSum = reversed(str(rawSum))

        return revertSum

    def makeListNode(self):
        return ListNode(next=self.makeListNode())

# if __name__ == '__main__':
#     # l1, l2 = Solution.addTwoNumbers(l1=ListNode(val=2, next=
#     #                                 ListNode(val=4, next=
#     #                                          ListNode(val=3))),
#     #                        l2=ListNode(val=5, next=
#     #                                 ListNode(val=6, next=
#     #                                          ListNode(val=4))))
#     #
#     #
#     # l1reverse = Solution.reversalLinkedList(l1)
#     # l2reverse = Solution.reversalLinkedList(l2)
#     #
#     # l1revExtr = Solution.extractValues(l1reverse)
#     # l2revExtr = Solution.extractValues(l2reverse)
#     #
#     # rawSum = l1revExtr + l2revExtr
#
#     # inp_string = str(input('please input'))
#     # inp_string = inp_string.replace('{', '(')
#     # inp_string = inp_string.replace('}', ')')
#     # inp_string = inp_string.replace(': ', '=')
#     # inp_string = inp_string.replace(', ', ',')
#     # inp_list = inp_string.split()
#     #
#
#     print(Solution.addTwoNumbers(inp_list))

#  ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}} ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}}
