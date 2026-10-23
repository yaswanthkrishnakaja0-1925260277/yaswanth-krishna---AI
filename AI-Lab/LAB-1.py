import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    """Manhattan distance from each tile to its goal position."""
    distance = 0
    for index, tile in enumerate(state):
        if tile != 0:
            goal_index = tile - 1
            distance += abs(index // 3 - goal_index // 3)
            distance += abs(index % 3 - goal_index % 3)
    return distance

def neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            board = list(state)
            board[zero], board[new_index] = board[new_index], board[zero]
            yield tuple(board)

def solve(start):
    frontier = [(heuristic(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while frontier:
        _, current_cost, state = heapq.heappop(frontier)

        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        if current_cost != cost[state]:
            continue

        for next_state in neighbors(state):
            new_cost = current_cost + 1
            if new_cost < cost.get(next_state, float("inf")):
                cost[next_state] = new_cost
                parent[next_state] = state
                heapq.heappush(
                    frontier,
                    (new_cost + heuristic(next_state), new_cost, next_state)
                )

    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
solution = solve(start)

if solution:
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()
else:
    print("No solution found.")
