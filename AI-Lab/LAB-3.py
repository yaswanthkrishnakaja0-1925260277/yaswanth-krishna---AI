from collections import deque

CAPACITY_1 = 4
CAPACITY_2 = 3
TARGET = 2

def get_next_states(state):
    a, b = state

    # Fill either jug
    yield (CAPACITY_1, b), "Fill 4-liter jug"
    yield (a, CAPACITY_2), "Fill 3-liter jug"

    # Empty either jug
    yield (0, b), "Empty 4-liter jug"
    yield (a, 0), "Empty 3-liter jug"

    # Pour 4-liter jug into 3-liter jug
    amount = min(a, CAPACITY_2 - b)
    yield (a - amount, b + amount), "Pour 4-liter into 3-liter"

    # Pour 3-liter jug into 4-liter jug
    amount = min(b, CAPACITY_1 - a)
    yield (a + amount, b - amount), "Pour 3-liter into 4-liter"

def solve():
    start = (0, 0)
    queue = deque([start])
    parent = {start: (None, "Start")}

    while queue:
        state = queue.popleft()
        a, b = state

        if a == TARGET or b == TARGET:
            path = []
            while state is not None:
                previous, action = parent[state]
                path.append((state, action))
                state = previous
            return path[::-1]

        for next_state, action in get_next_states(state):
            if next_state not in parent:
                parent[next_state] = (state, action)
                queue.append(next_state)

    return None

solution = solve()
if solution:
    for state, action in solution:
        print(f"{action}: {state}")
else:
    print("No solution found.")
