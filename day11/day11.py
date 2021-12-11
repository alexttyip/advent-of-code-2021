import itertools

n = 10


def flash(ints):
    num_flash = 0
    for i in range(n):
        for j in range(n):
            v = ints[i][j]

            if v < 0:
                continue

            if v > 9:
                num_flash += 1
                ints[i][j] = -10
                for (di, dj) in itertools.product([-1, 0, 1], repeat=2):
                    if di == 0 and dj == 0:
                        continue

                    if i + di not in range(n) or j + dj not in range(n):
                        continue

                    if ints[i + di][j + dj] in range(10):
                        ints[i + di][j + dj] += 1

    return ints, num_flash


def step(ints):
    for i in range(n):
        for j in range(n):
            ints[i][j] += 1

    ints, num_flash = flash(ints)

    while any(v > 9 for row in ints for v in row):
        ints, temp_flash = flash(ints)
        num_flash += temp_flash

    is_all_0 = True
    for i in range(n):
        for j in range(n):
            if ints[i][j] < 0:
                ints[i][j] = 0
            else:
                is_all_0 = False

    return ints, num_flash, is_all_0


def main():
    ints = [[int(i) for i in line.strip()] for line in open("input.txt")]

    part1 = part2 = 0

    simul = False
    while not simul:
        ints, temp_flash, simul = step(ints)
        if part2 < 100:
            part1 += temp_flash
        part2 += 1

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
