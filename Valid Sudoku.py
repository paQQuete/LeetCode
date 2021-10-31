class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        possdigits = frozenset([str(x) for x in range(1, 10)])
        checkDigit = list()
        dictStolbecListvalues = {i: list() for i in range(0, 9)}
        checkMatrix = [[[[i for i in range(0, 3)] for i in range(0,3)] for i in range(0, 3)] for i in range(0, 3)]
        i, j, k = 0
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

        # формируем словарь матриц 3х3 и сразу проверяем, переходим к новой матрице и т.д.




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
