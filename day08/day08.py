part1 = part2 = 0

for line in open("input.txt", "r"):
    line = line.replace("|", " ").strip().split()
    line = [set(v) for v in line]
    patterns = line[:10]
    outputs = line[10:]

    unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}
    one, four = set(), set()
    for v in patterns:
        if len(v) == 2:
            one = v
        elif len(v) == 4:
            four = v

    for (i, digit) in enumerate(outputs):
        value = 0

        if len(digit) in unique_lengths:
            value = unique_lengths[len(digit)]
            part1 += 1
        elif len(digit) == 5:
            if digit.issuperset(one):
                value = 3
            elif len(digit & four) == 2:
                value = 2
            else:
                value = 5
        else:
            if not digit.issuperset(one):
                value = 6
            elif digit.issuperset(four):
                value = 9
            else:
                value = 0

        part2 += value * 10 ** (3 - i)

print(part1)
print(part2)
