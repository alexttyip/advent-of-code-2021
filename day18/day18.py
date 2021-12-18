from typing import List


def parse(line: str, curr_idx: int = 0) -> List:
    line = line[1:-1]

    depth = 0
    pointer = 0
    curr = line[pointer]
    left = ""
    while pointer < len(line) and (depth > 0 or curr != ","):
        left += curr

        if curr == "[":
            depth += 1
        elif curr == "]":
            depth -= 1

        pointer += 1
        curr = line[pointer]

    curr_idx += 1
    if left.isdigit():
        left = [int(left)]
    else:
        left = parse(left, curr_idx)

    right_idx = curr_idx + len(left)
    nodes = [(curr_idx, right_idx)] + left

    right = line[pointer + 1:]
    if right.isdigit():
        right = [int(right)]
    else:
        right = parse(right, right_idx)

    nodes += right

    return nodes


def add(nodes: List, line: str):
    if not nodes:
        return parse(line)

    existing = []
    n = len(nodes)
    for node in nodes:
        if isinstance(node, tuple):
            existing.append((node[0] + 1, node[1] + 1))
        else:
            existing.append(node)

    return [(1, n + 1)] + existing + parse(line, n + 1)


def get_depth(nodes: List, idx=0) -> tuple:
    curr = nodes[idx]

    if isinstance(curr, int):
        return 0, -1

    left_idx, right_idx = curr

    if isinstance(nodes[left_idx], int) and isinstance(nodes[right_idx], int):
        return 1, idx

    left_depth, left_idx = get_depth(nodes, left_idx)
    right_depth, right_idx = get_depth(nodes, right_idx)

    if left_depth >= right_depth:
        return left_depth + 1, left_idx
    else:
        return right_depth + 1, right_idx


def explode(nodes: List, max_idx: int):
    left_idx, right_idx = nodes[max_idx]
    left = nodes[left_idx]
    right = nodes[right_idx]

    nodes[max_idx] = 0
    del nodes[right_idx]
    del nodes[left_idx]

    for idx in range(len(nodes)):
        if isinstance(nodes[idx], int):
            continue

        idx1, idx2 = nodes[idx]

        if idx1 > right_idx:
            idx1 -= 2
        elif idx1 > left_idx:
            idx1 -= 1

        if idx2 > right_idx:
            idx2 -= 2
        elif idx2 > left_idx:
            idx2 -= 1

        nodes[idx] = idx1, idx2

    if max_idx > right_idx:
        max_idx -= 2
    elif max_idx > left_idx:
        max_idx -= 1

    curr = max_idx - 1
    while curr >= 0 and isinstance(nodes[curr], tuple):
        curr -= 1

    if curr >= 0:
        nodes[curr] += left

    curr = max_idx + 1
    while curr < len(nodes) and isinstance(nodes[curr], tuple):
        curr += 1

    if curr < len(nodes):
        nodes[curr] += right


def step(nodes: List):
    new_nodes = nodes.copy()
    depth, max_idx = get_depth(new_nodes)

    if depth > 4:
        explode(new_nodes, max_idx)
        return step(new_nodes)

    idx = next((i for i, v in enumerate(new_nodes) if isinstance(v, int) and v >= 10), None)

    if idx is None:
        return new_nodes

    for i in range(len(new_nodes)):
        if isinstance(new_nodes[i], int):
            continue

        left, right = new_nodes[i]
        if left > idx:
            left += 2

        if right > idx:
            right += 2

        new_nodes[i] = left, right

    new_items = [
        (idx + 1, idx + 2),
        new_nodes[idx] // 2,
        new_nodes[idx] // 2 + (1 if new_nodes[idx] % 2 == 1 else 0)
    ]

    new_nodes = new_nodes[:idx] + new_items + new_nodes[idx + 1:]

    return step(new_nodes)


def cal_mag(nodes: List, idx: int = 0):
    if isinstance(nodes[idx], int):
        return nodes[idx]

    left, right = nodes[idx]

    left = cal_mag(nodes, left)
    right = cal_mag(nodes, right)

    return 3 * left + 2 * right


def main():
    lines = [line.strip() for line in open("input.txt").read().strip().split("\n")]

    part1 = []
    mag = 0
    for i in range(len(lines)):
        part1 = step(add(part1, lines[i]))
        nodes_i = parse(lines[i])
        for j in range(len(lines)):
            if i == j:
                continue

            nodes = step(add(nodes_i, lines[j]))

            mag = max(mag, cal_mag(nodes))

    print(cal_mag(part1))
    print(mag)


if __name__ == '__main__':
    main()
