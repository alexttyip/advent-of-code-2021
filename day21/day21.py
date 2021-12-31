from functools import cache


def part1(pos, score, player=0):
    i = 1
    rolled = 0
    while max(score) < 1000:
        pos[player] = (pos[player] + (i + 1) * 3 - 1) % 10 + 1

        score[player] += pos[player]

        rolled += 3

        player = not player
        i += 3

    return min(score) * rolled


@cache
def part2(players):
    wins = [s >= 21 for _, s in players]
    if sum(wins):
        return wins

    (curr_p, curr_s), other = players
    wins = [0, 0]

    dice = range(1, 4)

    for i in dice:
        for j in dice:
            for k in dice:
                temp_p = (curr_p + i + j + k - 1) % 10 + 1
                temp_s = curr_s + temp_p

                w2_, w1_ = part2((other, (temp_p, temp_s)))
                wins[0] += w1_
                wins[1] += w2_

    return wins


_, start1, _, start2 = open("input.txt").read().strip().replace("\n", ": ").split(": ")

print(part1([int(start1), int(start2)], [0, 0]))

p2 = part2(((int(start1), 0), (int(start2), 0)))
print(max(p2))
