import heapq

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"D": 2, "E": 5},
    "C": {"F": 3},
    "D": {"G": 4},
    "E": {"G": 2},
    "F": {"G": 2},
    "G": {}
}

heuristic = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 4,
    "E": 2,
    "F": 2,
    "G": 0
}

def a_star(start, goal):
    frontier = [(heuristic[start], 0, start)]
    parent = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current_cost, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], cost_so_far[goal]

        if current_cost != cost_so_far[current]:
            continue

        for neighbor, edge_cost in graph[current].items():
            new_cost = current_cost + edge_cost

            if new_cost < cost_so_far.get(neighbor, float("inf")):
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (priority, new_cost, neighbor))

    return None, float("inf")

path, total_cost = a_star("A", "G")

if path:
    print("Path:", " -> ".join(path))
    print("Total cost:", total_cost)
else:
    print("No path found.")
