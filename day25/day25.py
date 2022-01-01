import itertools

lines = open("input.txt").readlines()

right = set()
down = set()
for i, line in enumerate(lines):
    for j, c in enumerate(line.strip()):
        if c == ">":
            right.add((i, j))
        elif c == "v":
            down.add((i, j))

ni, nj = len(lines), len(lines[0].strip())

for count in itertools.count(1):
    new_right = {c if (c := (i, (j + 1) % nj)) not in right and c not in down else (i, j) for i, j in right}
    new_down = {c if (c := ((i + 1) % ni, j)) not in new_right and c not in down else (i, j) for i, j in down}

    if right == new_right and down == new_down:
        print(count)
        break

    right = new_right
    down = new_down
