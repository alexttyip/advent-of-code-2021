part1 = part2 = 0
n = 1000
plane = [[0] * n for _ in range(n)]
plane2 = [[0] * n for _ in range(n)]

for line in open("input.txt", "r"):
    x1, y1, x2, y2 = [int(i) for i in line.replace(" -> ", ",").split(",")]

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            plane[x1][i] += 1
            plane2[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            plane[i][y1] += 1
            plane2[i][y1] += 1
    else:
        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1
        range_x = range(x1, x2 + step_x, step_x)
        range_y = range(y1, y2 + step_y, step_y)

        for i, j in zip(range_x, range_y):
            plane2[i][j] += 1

for i in range(n):
    for j in range(n):
        if plane[i][j] >= 2:
            part1 += 1
        if plane2[i][j] >= 2:
            part2 += 1

print(part1)
print(part2)
