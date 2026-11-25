# 1. Map Coloring using CSP (backtracking)
colors = ["Red", "Green", "Blue"]
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

def solve(assignment):
    if len(assignment) == len(neighbors):
        return assignment

    region = next(r for r in neighbors if r not in assignment)
    for color in colors:
        if all(assignment.get(n) != color for n in neighbors[region]):
            result = solve({**assignment, region: color})
            if result:
                return result
    return None

print("Map coloring:", solve({}))
