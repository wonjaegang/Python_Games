board = [[], [], [], [], [], [], [], [], [], []]


def first_board():
    for i in range(10):
        for k in range(10):
            board[i].append(" □")


def set_board(location, color):
    x_location = ord(location[0]) - 65
    y_location = int(location[1])
    if color == "black":
        board[y_location][x_location] = " ◎"
    if color == "white":
        board[y_location][x_location] = " ●"


def print_board():
    print("   A  B  C  D  E  F  G  H  I  J")
    for i in range(10):
        line = ""
        for k in range(10):
            line += board[i][k]
        print(str(i) + line)


def win_the_game():
    for i in range(10):
        for k in range(10):
            if board[i][k] == " ◎":
                for n in range(4):
                    continuous = 1
                    if i + (int(n / (n - 0.1))) * 4 <= 9 and 0 <= k + (1 - n % 3) * 4 <= 9:
                        for m in range(4):
                            if board[i + (int(n / (n - 0.1))) * (m + 1)][k + (1 - n % 3) * (m + 1)] == " ◎":
                                continuous += 1
                                if continuous == 5:
                                    return "black win"
            if board[i][k] == " ●":
                for n in range(4):
                    continuous = 1
                    if i + (int(n / (n - 0.1))) * 4 <= 9 and 0 <= k + (1 - n % 3) * 4 <= 9:
                        for m in range(4):
                            if board[i + (int(n / (n - 0.1))) * (m + 1)][k + (1 - n % 3) * (m + 1)] == " ●":
                                continuous += 1
                                if continuous == 5:
                                    return "white win"
    return "not end"


first_board()
print_board()
turn = 1
while win_the_game() == "not end":
    if turn % 2 == 1:
        location_input = input("Black's turn. Enter a location. ex)B7 : ")
        set_board(location_input, "black")
    if turn % 2 == 0:
        location_input = input("White's turn. Enter a location. ex)B7 : ")
        set_board(location_input, "white")
    print_board()
    turn += 1
if win_the_game() == "black win":
    print("Game Over. Black Win!")
if win_the_game() == "white win":
    print("Game Over. White Win!")
