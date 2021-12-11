from typing import List


def find_basin(queue: List[tuple], ints, explored):
    if not queue:
        return explored

    i, j = queue.pop(0)
    for offset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new_i = i + offset[0]
        new_j = j + offset[1]

        if new_i not in range(len(ints)) or new_j not in range(len(ints[0])):
            continue

        if (new_i, new_j) not in explored and ints[new_i][new_j] != 9:
            explored.add((new_i, new_j))
            queue.append((new_i, new_j))

    return find_basin(queue, ints, explored)


def main():
    lines = open("input.txt", "r").readlines()
    ints = [[int(i) for i in line.strip()] for line in lines]

    part1 = 0
    part2 = 1

    basins = []
    low_points = []

    for (i, row) in enumerate(ints):
        for (j, v) in enumerate(row):
            is_lowest = True
            for offset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_i = i + offset[0]
                new_j = j + offset[1]
                if new_i in range(len(ints)) and new_j in range(len(row)):
                    is_lowest = is_lowest and v < ints[new_i][new_j]

            if is_lowest:
                part1 += v + 1
                low_points.append((i, j))

    for p in low_points:
        basins.append(find_basin([p], ints, set()))

    for basin in sorted(basins, key=len, reverse=True)[:3]:
        part2 *= len(basin)

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
