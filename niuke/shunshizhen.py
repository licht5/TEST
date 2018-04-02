# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrixCircle(self, matrix, rows, columns, start):
        endx = columns - 1 - start
        endy = rows - 1 - start
        for i in range(start, endx + 1):
            print(matrix[start][i])
        if (start < endy):
            for i in range(start + 1, endy + 1):
                print(matrix[i][endx])
        if (start < endy and start < endx):
            for i in reversed(range(start, endx)):
                print(matrix[endy][i])
        if (start < endy - 1 and start < endx):
            for i in reversed(range(start + 1, endy)):
                print(matrix[i][start])

    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        columns = len(matrix[0])
        if (matrix == None):
            return
        start = 0
        while (columns > start * 2 and rows > start * 2):
            self.printMatrixCircle(matrix, rows, columns, start)
            start = start + 1

if __name__ == '__main__':
  s=Solution()
  s.printMatrix([[1,2],[3,4]])