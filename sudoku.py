"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
"""


def sudoku(board: list) -> list:
    squares = [[] for i in range(9)]
    columns = [[] for i in range(9)]

    for i in range(9):
        for j in range(9):
            columns[i].append(board[j][i])

    i = 0
    j = 0
    s = 0
    the_list = [2, 5, 8]

    while True:
        if i in the_list and j == 8:
            if i == 8 and j == 8:
                squares[s].append(board[i][j])
                break
            squares[s].append(board[i][j])
            s += 1
            i += 1
            j = 0

        elif j in the_list and i not in the_list:
            squares[s].append(board[i][j])
            i += 1
            j -= 2

        elif j in the_list and i in the_list:
            squares[s].append(board[i][j])
            i -= 2
            j += 1
            s += 1

        else:
            squares[s].append(board[i][j])
            j += 1

    i = 0
    j = 0
    s = 0
    idex = 0
    dictionary = {}

    while True:
        # new line and new square
        if i in the_list and j == 8:
            if i == 8 and j == 8:
                dictionary[f"{str(i) + str(j)}"] = [s, idex]
                break
            dictionary[f"{str(i) + str(j)}"] = [s, idex]
            idex = 0
            s += 1
            i += 1
            j = 0

        # new line in square
        elif j in the_list and i not in the_list:
            dictionary[f"{str(i) + str(j)}"] = [s, idex]
            i += 1
            j -= 2
            idex += 1

        # new square
        elif j in the_list and i in the_list:
            dictionary[f"{str(i) + str(j)}"] = [s, idex]
            i -= 2
            j += 1
            s += 1
            idex = 0

        # usual statement
        else:
            dictionary[f"{str(i) + str(j)}"] = [s, idex]
            j += 1
            idex += 1

    i = 0

    while i < 9:
        j = 0
        while j < 9:
            if board[i][j] != ".":
                j += 1
                continue

            square_index = dictionary[f"{str(i) + str(j)}"][0]

            temp_list = []
            for index in range(1, 10):
                number = str(index)
                if (number not in board[i] and
                    number not in columns[j] and
                    number not in squares[square_index]):

                    temp_list.append(number)

            if len(temp_list) == 1:
                board[i][j] = temp_list[0]
                columns[j][i] = temp_list[0]
                in_square_idx = dictionary[f"{str(i) + str(j)}"][1]
                squares[square_index][in_square_idx] = temp_list[0]

            temp_list = []
            j += 1

        i += 1

        if i >= 9 and j >= 9:
            for k in range(9):
                for z in range(9):
                    if board[k][z] == ".":
                        i = 0
                        j = 0

            if i != 0 or j != 0:
                break

    return board


custom_board = [[] for i in range(9)]
custom = False
quest = str(input("Is board custom? (y for yes / n for no.)\n"))

while True:
    if quest == "n":
        print("No.")
        break
    elif quest == "y":
        custom = True
        print("Input your sudoku to be solved:")
        for o in range(9):
            for p in range(9):
                new = str(input())
                while True:
                    if new.isdigit() or new == ".":
                        custom_board[o].append(new)
                        break
                    else:
                        print("Invalid literal.")
                        new = str(input())
        break
    else:
        print("Invalid literal.")
        quest = str(input())

the_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

if custom:
    the_board = custom_board
    print("Your sudoku is: ")
    print(" ----------------------------------------------")
    for row in custom_board:
        for digit in row:
            print(" | ", digit, end="")
        print(" | \n", "----------------------------------------------")


new_board = sudoku(the_board)

print(" ----------------------------------------------")
for row in new_board:
    for digit in row:
        print(" | ", digit, end="")
    print(" | \n", "----------------------------------------------")
