rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

while "Dirty" in rooms.values():
    print(f"Vacuum is in room {location}")

    if rooms[location] == "Dirty":
        rooms[location] = "Clean"
        print(f"Cleaned room {location}")

    elif location == "A":
        location = "B"
        print("Moved to room B")

    else:
        location = "A"
        print("Moved to room A")

print("All rooms are clean.")
print(rooms)
