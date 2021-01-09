board = [[], [], [], [], [], [], [], [],]


def first_board():
    for i in range(8):
        for k in range(8):
            board[i].append(" □")


def set_board(location, color):
    x_location = ord(location[0]) - 65
    y_location = int(location[1])
    board[y_location][x_location] = color
    for i in range(9):
        blank_marker = 1
        for m in range(7):
            if 0 <= x_location + (i % 3 - 1) * (m + 1) <= 7 and 0 <= y_location + (int(i / 3) - 1) * (m + 1) <= 7:
                if board[y_location + (int(i / 3) - 1) * (m + 1)][x_location + (i % 3 - 1) * (m + 1)] == " □":
                    blank_marker = 0
                if board[y_location + (int(i / 3) - 1) * (m + 1)][x_location + (i % 3 - 1) * (m + 1)] == color:
                    for n in range(m * blank_marker):
                        board[y_location + (int(i / 3) - 1) * (n + 1)][x_location + (i % 3 - 1) * (n + 1)] = color
                    break


def print_board():
    print("   A  B  C  D  E  F  G  H")
    for i in range(8):
        line = ""
        for k in range(8):
            line += board[i][k]
        print(str(i) + line)


def result():
    blank = 0
    black = 0
    white = 0
    for i in range(8):
        for k in range(8):
            if board[i][k] == " □":
                blank += 1
            if board[i][k] == " ◎":
                black += 1
            if board[i][k] == " ●":
                white += 1
    return [blank, black, white]


first_board()
set_board("D3", " ◎")
set_board("E4", " ◎")
set_board("D4", " ●")
set_board("E3", " ●")
print_board()
print("Black : " + str(result()[1]) + ", White : " + str(result()[2]))
turn = 1
while not result()[0] == 0:
    if turn % 2 == 1:
        location_input = input("Black's turn. Enter a location. ex)B7 : ")
        set_board(location_input, " ◎")
    if turn % 2 == 0:
        location_input = input("White's turn. Enter a location. ex)B7 : ")
        set_board(location_input, " ●")
    print_board()
    print("Black : " + str(result()[1]) + ", White : " + str(result()[2]))
    turn += 1
if result()[1] > result()[2]:
    print("Black win!")
if result()[1] < result()[2]:
    print("White win!")
if result()[1] == result()[2]:
    print("Draw!")
