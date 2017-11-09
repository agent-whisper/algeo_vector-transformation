class Matrix:
    def __init__(self, rowSize, columnSize):
        self.matrix = []

        for i in range(columnSize):
            aColumn = []
            for j in range(rowSize):
                aColumn += [None]

            self.matrix += [aColumn]

    def setValue(self, value, rowPos, colPos):
        self.matrix[colPos][rowPos] = value

def multiplyMatrix(m1, m2):
    rowSize = len(m1[0])
    columnSize = len(m2)
    inBetween = len(m1)
    temp = Matrix(rowSize, columnSize)
    for i in range(rowSize):
        for j in range(columnSize):
            sum = 0
            for k in range(inBetween):
                sum += m1[k][i] * m2[j][k]
            temp.setValue(sum, i, j)

    result = temp.matrix[:]
    return result


