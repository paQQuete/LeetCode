class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        possdigits = frozenset([str(x) for x in range(1, 10)])
        checkDigit = list()
        dictStolbecListvalues = {i: list() for i in range(0, 9)}
        checkMatrix = [[[[i for i in range(0, 3)] for i in range(0,3)] for i in range(0, 3)] for i in range(0, 3)]

        dictMatrixs = {i: list() for i in range(0, 9)}

        # проверка повторений в строках доски
        for stroka in board:
            for i in range(0, len(stroka)):
                if stroka[i] in possdigits and stroka[i] in checkDigit:
                    return False
                else:
                    checkDigit.append(stroka[i])
            checkDigit = list()

        # формируем словарь, иднекс столбца: список значений столбца
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                dictStolbecListvalues[j].append(board[i][j])

        # проверяем столбцы на дубли символов
        for key, value in dictStolbecListvalues.items():
            for i in range(0, len(value)):
                if value[i] in possdigits and value[i] in checkDigit:
                    return False
                else:
                    checkDigit.append(value[i])
            checkDigit = list()

        # нарезаем борду по спискам с 3 элементами, т.е. режем строку на 3, очищаем и кладём 3 списка (по 3 эл. в каждом)
        for stroka in board:
            list1stElement = stroka[0:3]
            list2ndElement = stroka[3:6]
            list3rdElement = stroka[6:9]
            stroka.clear()
            stroka.append(list1stElement)
            stroka.append(list2ndElement)
            stroka.append(list3rdElement)

        # i = 0
        # matrixCount = 0
        # while i < 3: #итератор по столбцам!
        #     for line in board:
        #         for eachElement in line[i]:
        #             if eachElement in possdigits and eachElement in checkDigit:
        #                 return False
        #             else:
        #                 checkDigit.append(eachElement)
        #         matrixCount += 1
        #         if matrixCount >= 3:
        #             pass
        #
        # temp3x3matrix = list()
        # matrixCount = 0
        # j = 0 #итератор столбца
        # i = 0 #итератор линии в старой борде
        # while True:
        #     temp3x3matrix.append(board[i][j])
        #     pass
        #
        unsortedMatrixList = [[[],[],[]] for x in range(0,3)]
        usedLineCount = 0
        listStringBoard = str()
        for line in board:
            for oneThird in line:
                for each in oneThird:
                    listStringBoard += each

        listStringBoard = list(listStringBoard)

        # пихаем все знаки поля 3х3 в отдельные списки
        matrixNumber = 0
        while listStringBoard:

            for stroka in unsortedMatrixList:
                for i in range(0,9):
                    for j in range(0,3):
                        stroka[matrixNumber].append(listStringBoard.pop(0))
                    matrixNumber += 1
                    if matrixNumber == 3:
                        matrixNumber = 0

        # проверяем каждое поле 3х3 по сформированным спискам
        for stroka in unsortedMatrixList:
            for eachMatrix in stroka:
                for eachElem in eachMatrix:
                    if eachElem in checkDigit and eachElem in possdigits:
                        return False
                    else:
                        checkDigit.append(eachElem)
                checkDigit = list()


        return True


if __name__ == '__main__':
    brd = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().isValidSudoku(brd))
