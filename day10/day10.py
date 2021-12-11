from collections import Counter


def main():
    lines = open("input.txt", "r")

    part1 = 0

    corrupt = []
    incomplete = []

    for line in lines:
        stack = []
        is_corrupt = False
        for c in line.strip():
            if not stack:
                stack.append(c)
                continue

            match c:
                case '(' | '[' | '{' | '<':
                    stack.append(c)

                case _:
                    tail = stack.pop()
                    if (tail + c) not in ["()", "[]", "{}", "<>"]:
                        corrupt.append(c)
                        is_corrupt = True
                        break

        score = 0
        if not is_corrupt:
            for c in reversed(stack):
                score *= 5
                match c:
                    case '(':
                        score += 1
                    case '[':
                        score += 2
                    case '{':
                        score += 3
                    case '<':
                        score += 4
            incomplete.append(score)

    corrupt = Counter(corrupt)
    part1 += corrupt[')'] * 3
    part1 += corrupt[']'] * 57
    part1 += corrupt['}'] * 1197
    part1 += corrupt['>'] * 25137

    part2 = sorted(incomplete)[len(incomplete) // 2]

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
