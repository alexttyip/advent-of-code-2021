import math


def pop(packet, n):
    return parse_bin(packet[:n]), packet[n:]


def parse_bin(v):
    return int(v, 2)


# noinspection PyPep8Naming
def packet_operation(packet):
    V, packet = pop(packet, 3)
    T, packet = pop(packet, 3)

    if T == 4:
        value = ""
        curr = "1"
        while curr[0] == "1":
            curr, packet = packet[:5], packet[5:]

            value += curr[1:]

        return V, parse_bin(value), packet

    I, packet = pop(packet, 1)

    if I == 0:
        L, packet = pop(packet, 15)
        rest, packet = packet[:L], packet[L:]
    else:
        L, rest = pop(packet, 11)

    value = []
    count = 0
    while (I == 0 and rest) or (I == 1 and count < L):
        version, temp_value, rest = packet_operation(rest)
        V += version
        value.append(temp_value)
        count += 1

    if T == 0:
        value = sum(value)
    elif T == 1:
        value = math.prod(value)
    elif T == 2:
        value = min(value)
    elif T == 3:
        value = max(value)
    elif T == 5:
        value = value[0] > value[1]
    elif T == 6:
        value = value[0] < value[1]
    elif T == 7:
        value = value[0] == value[1]

    return V, value, packet if I == 0 else rest


def main():
    line = open("input.txt").read().strip()

    packet = format(int(line, 16), "b").zfill(4 * len(line))

    part1, part2, _ = packet_operation(packet)

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
