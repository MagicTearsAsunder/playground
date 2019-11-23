class Sudoku:
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        if not self.data:
            return False

        length = len(self.data)
        if length**.5 != int(length**.5):
            return False

        for i in self.data:
            if len(i) != length:
                return False

        columns = [[] for i in range(length)]
        squares = []

        for i in range(length):
            for j in range(length):
                columns[i].append(self.data[j][i])

        square = int(length**.5)
        for i in range(square):   # 1
            for j in range(square):  # 0
                temp = j*square
                new = []

                for m in range(square):
                    new.extend(self.data[i*square+m][temp:temp+square])

                squares.append(new)

        for i in range(length):  # 4
            for j, item in enumerate(self.data[i]):
                if item < 1 or item > length:
                    return False
                index = (i // square)*square + (j // square)
                if (self.data[i].count(item) != 1 or
                        columns[j].count(item) != 1 or
                        squares[index].count(item) != 1):
                    return False

        return True


if __name__ == "__main__":
    board = [
        [7, 8, 4,  1, 5, 9,  3, 2, 6],
        [5, 3, 9,  6, 7, 2,  8, 4, 1],
        [6, 1, 2,  4, 3, 8,  7, 5, 9],

        [9, 2, 8,  7, 1, 5,  4, 6, 3],
        [3, 5, 7,  8, 4, 6,  1, 9, 2],
        [4, 6, 1,  9, 2, 3,  5, 8, 7],

        [8, 7, 6,  3, 9, 4,  2, 1, 5],
        [2, 4, 3,  5, 6, 1,  9, 7, 8],
        [1, 9, 5,  2, 8, 7,  6, 3, 4]
    ]

    board2 = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]

    test_case = Sudoku(board)
    print(test_case.is_valid())
