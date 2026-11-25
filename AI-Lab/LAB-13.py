# 3. Minimax for Tic-Tac-Toe
LINES = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
         (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def winner(board, player):
    return any(all(board[i] == player for i in line) for line in LINES)

def minimax(board, maximizing):
    if winner(board, "X"): return 1
    if winner(board, "O"): return -1
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "X" if maximizing else "O"
            scores.append(minimax(board, not maximizing))
            board[i] = " "
    return max(scores) if maximizing else min(scores)

board = ["X", "O", "X", " ", "O", " ", " ", " ", " "]
print("Best score for X:", minimax(board, True))
