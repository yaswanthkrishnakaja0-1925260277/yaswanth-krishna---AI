# 4. Alpha-Beta pruning
def alphabeta(node, depth, alpha, beta, maximizing):
    if depth == 0 or isinstance(node, int):
        return node

    if maximizing:
        value = float("-inf")
        for child in node:
            value = max(value, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for child in node:
            value = min(value, alphabeta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

tree = [[3, 5], [2, 9]]
print("Best value:", alphabeta(tree, 2, float("-inf"), float("inf"), True))
