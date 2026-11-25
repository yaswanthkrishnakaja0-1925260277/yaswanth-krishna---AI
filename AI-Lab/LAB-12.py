# 2. Tic-Tac-Toe game
board = [" "] * 9
lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
         (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

for turn in range(9):
    player = "X" if turn % 2 == 0 else "O"

    for row in range(0, 9, 3):
        print("|".join(board[row:row+3]))

    move = int(input(f"{player}, enter position (0-8): "))
    if not 0 <= move < 9 or board[move] != " ":
        print("Invalid move; try again.")
        continue

    board[move] = player
    if any(all(board[i] == player for i in line) for line in lines):
        print(player, "wins!")
        break
else:
    print("Draw!")
