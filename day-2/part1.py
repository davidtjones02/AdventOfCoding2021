position = {"horizontal": 0, "depth": 0}


with open("commands.txt", "r") as file:
    # read each line and see if it contains horizontal or depth
    for line in file:
        print(line)
        if "forward" in line:
            position["horizontal"] += int(line.split()[1])
        elif "up" in line:
            position["depth"] -= int(line.split()[1])
        else:
            position["depth"] += int(line.split()[1])


# multiply position horiziontal with position depth
print(position["horizontal"] * position["depth"])

# print(methods)
