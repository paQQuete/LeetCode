class Solution:
    def isPalindrome(self, n1: int) -> bool:
        n2 = 0
        inputNumber = n1

        if n1 == 0:
            return True
        elif n1 < 0:
            return False

        while n1 > 0:
            # находим остаток - последнюю цифру
            digit = n1 % 10
            # делим нацело - удаляем последнюю цифру
            n1 = n1 // 10
            # увеличиваем разрядность второго числа
            n2 = n2 * 10
            # добавляем очередную цифру
            n2 = n2 + digit

        if inputNumber == n2:
            return True
        else:
            return False

        '''
        можно улучшить - гнать алгоритм до середины числа и сравнивать половинки, а если число нечетное то выкидывать середину
        '''



if __name__ == '__main__':
    print(Solution().isPalindrome(-323))