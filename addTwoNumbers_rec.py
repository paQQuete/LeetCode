import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, inp):

        l1, l2 = self.input_parse(inp)

        l1 = eval(l1)
        l2 = eval(l2)

        current1, current2 = l1, l2
        output = None
        next_step_value = 0

        while (current1 != None or current2 != None):

            if current1 == None:
                current1 = ListNode(0)
            elif current2 == None:
                current2 = ListNode(0)

            sum = int(current1.val) + int(current2.val) + next_step_value
            next_step_value = 0
            if sum >= 10:
                sumStr = str(sum)
                next_step_value = int(sumStr[0])
                sum = int(sumStr[1])

            current1, current2 = current1.next, current2.next

            output = ListNode(sum, output)
        else:
            if next_step_value > 0:
                output = ListNode(next_step_value, output)

        output = self.reversalLinkedList(output)

        return output

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

    def input_parse(self, inp_string):
        inp_string = inp_string.replace('{', '(')
        inp_string = inp_string.replace('}', ')')
        inp_string = inp_string.replace(': ', '=')
        inp_string = inp_string.replace(', ', ',')
        inp_list = inp_string.split()

        return inp_list


if __name__ == '__main__':
    Solution().addTwoNumbers(inp=input('please input'))

# ListNode{val: 9, next: ListNode{val: 8, next: ListNode{val: 5, next: None}}} ListNode{val: 5, next: ListNode{val: 6, next: None}}
