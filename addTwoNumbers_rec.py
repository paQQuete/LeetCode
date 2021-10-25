import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        l1 = eval(self.input_parse(l1))
        l2 = eval(self.input_parse(l2))

        current1, current2 = l1, l2
        output = ListNode()
        output_current = None
        next_step_value = 0
        i = 0

        while current1 or current2 is not None:

            sum = int(current1.val) + int(current2.val) + next_step_value
            if sum >= 10:
                sumStr = str(sum)
                next_step_value = int(sumStr[0])
                sum = int(sumStr[1])

            if i == 0:
                output_current = output
                output_current.val = sum
                output_current.next = ListNode()

            else:
                output_current.val = sum
                output_current.next = ListNode()

            current1, current2 = current1.next, current2.next

        return output

    def input_parse(self, inp_string):
        inp_string = inp_string.replace('{', '(')
        inp_string = inp_string.replace('}', ')')
        inp_string = inp_string.replace(': ', '=')
        inp_string = inp_string.replace(', ', ',')
        inp_list = inp_string.split()

        return inp_string


if __name__ == '__main__':
    inp = Solution.input_parse(input('please input'))
    S
