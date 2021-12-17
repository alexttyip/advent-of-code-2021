def check(dx, dy, x1, x2, y1, y2):
    x, y = 0, 0

    while x <= x2 and y >= y1:
        x += dx
        y += dy

        if dx < 0:
            dx += 1
        elif dx > 0:
            dx -= 1

        dy -= 1

        if x in range(x1, x2 + 1) and y in range(y1, y2 + 1):
            return True

    return False


def main():
    _, x, _, y = open("input.txt").read().strip().replace(", ", "=").split("=")

    x1, x2 = tuple(map(int, x.split("..")))
    y1, y2 = tuple(map(int, y.split("..")))

    max_dy = abs(y1) - 1
    part1 = sum(range(1, max_dy + 1))

    min_dx = 1
    sum_foo = 1
    while sum_foo < x1:
        min_dx += 1
        sum_foo += min_dx

    part2 = 0
    for dx in range(min_dx, x2 + 1):
        for dy in range(y1, max_dy + 1):
            if check(dx, dy, x1, x2, y1, y2):
                part2 += 1

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
