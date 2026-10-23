from itertools import permutations

letters = "SENDMORY"
leading_letters = {"S", "M"}

for digits in permutations(range(10), len(letters)):
    assignment = dict(zip(letters, digits))

    if any(assignment[letter] == 0 for letter in leading_letters):
        continue

    send = (
        assignment["S"] * 1000
        + assignment["E"] * 100
        + assignment["N"] * 10
        + assignment["D"]
    )
    more = (
        assignment["M"] * 1000
        + assignment["O"] * 100
        + assignment["R"] * 10
        + assignment["E"]
    )
    money = (
        assignment["M"] * 10000
        + assignment["O"] * 1000
        + assignment["N"] * 100
        + assignment["E"] * 10
        + assignment["Y"]
    )

    if send + more == money:
        print(f"SEND  = {send}")
        print(f"MORE  = {more}")
        print(f"MONEY = {money}")
        print("Mapping:", assignment)
        break
else:
    print("No solution found.")
