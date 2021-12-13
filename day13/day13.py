from collections import defaultdict

plane = set()

part1 = -1

maxes = defaultdict(int)
coordinates, folds = open("input.txt").read().strip().split("\n\n")

for line in coordinates.split("\n"):
    x, y = list(map(int, line.split(",")))
    plane.add((x, y))
    maxes["x"] = max(x, maxes["x"])
    maxes["y"] = max(y, maxes["y"])

for line in folds.split("\n"):
    axis, v = line.split("=")
    axis = axis[-1:]
    v = int(v)

    offset = 0
    if v < maxes[axis] // 2:
        offset = 2 * v - maxes[axis]
        maxes[axis] -= v + 1
    else:
        maxes[axis] = v - 1

    if axis == "x":
        plane = {(x + offset, y) if x < v else (2 * v - x + offset, y) for (x, y) in plane}
    else:
        plane = {(x, y + offset) if y < v else (x, 2 * v - y + offset) for (x, y) in plane}

    if part1 == -1:
        part1 = len(plane)

print(part1)

for y in range(maxes["y"] + 1):
    for x in range(maxes["x"] + 1):
        print("#" if (x, y) in plane else ".", end=" ")
    print()
