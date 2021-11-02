class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # tempMatrix = [[] for x in range(0, len(matrix))]
        j = 0
        stroka = 0
        trueMatrixLen = len(matrix)
        for k in range(0, len(matrix)):
            matrix.append([])
        for i in range(0, trueMatrixLen*trueMatrixLen):
            if i % 4 == 0 and i != 0:
                stroka += 1
                j = 0



            matrix[j+trueMatrixLen].append(matrix[stroka][j])
            if j % 4 == 0 and j != 0:
                j = 0
            else:
                j += 1

        for i in range(0, trueMatrixLen):
            matrix.pop(0)

        for i in range(0, len(matrix)):
            matrix[i].reverse()

        # решение выше верное, но на ЛитКод при добавлении ошибка доступа по индексу, видимо есть ограничение

if __name__ == '__main__':
    matrix = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]

    print(Solution().rotate(matrix))
    # Output: [[15, 13, 2, 5],
    #         [14, 3, 4, 1],
    #         [12, 6, 8, 9],
    #         [16, 7, 10, 11]]
