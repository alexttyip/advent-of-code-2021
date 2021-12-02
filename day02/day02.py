lines = open("input.txt", "r").readlines()

# part 1
depth = 0
hori = 0
for line in lines:
    (command, x) = line.split(" ")
    if command == "forward":
        hori += int(x)
    elif command == "down":
        depth += int(x)
    else:
        depth -= int(x)
part1 = depth * hori

# part 2
depth = 0
hori = 0
aim = 0
for line in lines:
    (command, x) = line.split(" ")
    if command == "forward":
        hori += int(x)
        depth += int(x) * aim
    elif command == "down":
        aim += int(x)
    else:
        aim -= int(x)
part2 = depth * hori

print(part1)
print(part2)
