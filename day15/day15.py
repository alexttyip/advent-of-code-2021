import heapq as hq


def read_input(part2=False):
    lines = open("input.txt").readlines()

    n = len(lines)
    points = dict()

    if not part2:
        for i, line in enumerate(lines):
            for j, c in enumerate(line.strip()):
                points[(i, j)] = int(c)

        return points, n

    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            points.update({(i + k * n, j + m * n): (int(c) + k + m - 1) % 9 + 1 for k in range(5) for m in range(5)})

    n *= 5

    return points, n


def search(graph, n):
    heap = [(0, (0, 0))]
    seen = {(0, 0)}

    while heap:
        dist, (x, y) = hq.heappop(heap)

        if x == y == n - 1:
            return dist

        for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_p = x + dx, y + dy

            if not all(0 <= x < n for x in new_p) or new_p in seen:
                continue

            hq.heappush(heap, (dist + graph[new_p], new_p))
            seen.add(new_p)


print(search(*read_input()))
print(search(*read_input(True)))
