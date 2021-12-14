from collections import Counter, defaultdict


def cal_diff(pairs, tail):
    counter = Counter()
    for key, value in pairs.items():
        counter.update({key[0]: value})

    counter.update(tail)
    counter = counter.most_common()

    return counter[0][1] - counter[-1][1]


def main():
    p, inserts = open("input.txt").read().strip().split("\n\n")
    inserts = {lhs: rhs for lhs, rhs in (line.split(" -> ") for line in inserts.split("\n"))}

    part1 = dict()

    pairs = defaultdict(int)
    for i in range(len(p) - 1):
        pairs[p[i:i + 2]] += 1

    for i in range(40):
        for (s1, s2), value in pairs.copy().items():
            insert = inserts[s1 + s2]
            pairs[s1 + s2] -= value
            pairs[s1 + insert] += value
            pairs[insert + s2] += value

        if i == 9:
            part1 = pairs.copy()

    part1 = cal_diff(part1, p[-1])
    part2 = cal_diff(pairs, p[-1])

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
