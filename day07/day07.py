lines = open("input.txt", "r").readline().strip().split(",")
# lines = "16,1,2,0,4,2,7,1,2,14".strip().split(",")
ints = list(map(int, lines))

part1 = []
part2 = []

for dest in range(max(ints)):
    part1_temp = 0
    part2_temp = 0
    for i in ints:
        dist = abs(i - dest)
        part1_temp += dist
        part2_temp += (dist * (dist + 1)) // 2

    part1.append(part1_temp)
    part2.append(part2_temp)

print(min(part1))
print(min(part2))
