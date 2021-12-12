import typing
from collections import defaultdict
from typing import List


def traverse(curr: str, edges: typing.Dict[str, List[str]], path: List[str], has_revisited: bool) -> int:
    if curr == "end":
        return 1

    caves = edges[curr]

    paths = 0

    for cave in caves:
        if cave.islower() and cave in path:
            if not has_revisited:
                paths += traverse(cave, edges, path + [curr], True)
            continue

        paths += traverse(cave, edges, path + [curr], has_revisited)

    return paths


def main():
    edges = defaultdict(list)
    for lhs, rhs in (line.strip().split("-") for line in open("input.txt", "r")):
        edges[lhs].append(rhs)

        if lhs != "start" and rhs != "end":
            edges[rhs].append(lhs)

    part1 = traverse("start", edges, [], True)
    part2 = traverse("start", edges, [], False)

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
