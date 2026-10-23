from itertools import permutations

graph = {
    "A": {"B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30}
}

start = "A"
other_cities = [city for city in graph if city != start]

best_path = None
best_cost = float("inf")

for order in permutations(other_cities):
    route = [start] + list(order) + [start]
    cost = 0

    for i in range(len(route) - 1):
        cost += graph[route[i]][route[i + 1]]

    if cost < best_cost:
        best_cost = cost
        best_path = route

print("Best route:", " -> ".join(best_path))
print("Minimum cost:", best_cost)
