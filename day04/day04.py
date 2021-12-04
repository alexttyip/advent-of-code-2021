import typing


def check_num_exists(card: typing.List[typing.List[int]], num: int) -> (int, int):
    for (i, row) in enumerate(card):
        for (j, v) in enumerate(row):
            if v == num:
                return i, j

    return -1, -1


def check_bingo(holes: typing.List[typing.List[bool]]) -> bool:
    for i in range(5):
        if all(holes[i]) or all(row[i] for row in holes):
            return True

    return False


def cal_score(card: typing.List[typing.List[int]], holes: typing.List[typing.List[bool]], num: int) -> int:
    temp_score = 0
    for (i, row) in enumerate(card):
        for (j, v) in enumerate(row):
            if not holes[i][j]:
                temp_score += v

    return temp_score * num


def main():
    lines = open("input.txt", "r").readlines()

    nums = list(map(int, lines.pop(0).strip().split(",")))

    min_steps = len(nums) + 1
    max_steps = 0
    part1 = part2 = 0

    while len(lines) > 0:
        if lines[0].strip() == "":
            lines.pop(0)

        card = [[int(num) for num in lines.pop(0).split()] for _ in range(5)]
        holes = [[False] * 5 for _ in range(5)]

        for (idx, num) in enumerate(nums):
            (row, col) = check_num_exists(card, num)

            if row != -1 and col != -1:
                holes[row][col] = True

                if idx > 4 and check_bingo(holes):
                    if idx + 1 < min_steps:
                        min_steps = idx + 1
                        part1 = cal_score(card, holes, num)

                    if idx + 1 > max_steps:
                        max_steps = idx + 1
                        part2 = cal_score(card, holes, num)

                    break

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
