from collections import deque

TOTAL_MISSIONARIES = 3
TOTAL_CANNIBALS = 3
BOAT_CAPACITY = 2

# State: (missionaries_left, cannibals_left, boat_side)
# boat_side is 0 for left bank, 1 for right bank

def is_valid(missionaries, cannibals):
    if not (0 <= missionaries <= TOTAL_MISSIONARIES):
        return False
    if not (0 <= cannibals <= TOTAL_CANNIBALS):
        return False

    missionaries_right = TOTAL_MISSIONARIES - missionaries
    cannibals_right = TOTAL_CANNIBALS - cannibals

    if missionaries > 0 and cannibals > missionaries:
        return False
    if missionaries_right > 0 and cannibals_right > missionaries_right:
        return False

    return True

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    queue = deque([start])
    parent = {start: None}

    possible_passengers = [
        (1, 0), (2, 0), (0, 1), (0, 2), (1, 1)
    ]

    while queue:
        state = queue.popleft()

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        missionaries, cannibals, boat_side = state
        direction = -1 if boat_side == 0 else 1

        for m, c in possible_passengers:
            new_m = missionaries + direction * m
            new_c = cannibals + direction * c
            next_state = (new_m, new_c, 1 - boat_side)

            if is_valid(new_m, new_c) and next_state not in parent:
                parent[next_state] = state
                queue.append(next_state)

    return None

solution = solve()
if solution:
    for step, state in enumerate(solution):
        side = "Left" if state[2] == 0 else "Right"
        print(f"Step {step}: M={state[0]}, C={state[1]}, Boat={side}")
else:
    print("No solution found.")
