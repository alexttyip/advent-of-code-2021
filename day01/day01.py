numbers = list(map(int, open("input.txt", "r").readlines()))

# Part 1
part1 = sum([numbers[i] > numbers[i - 1] for i in range(len(numbers))])

# Part 2
part2 = sum([numbers[i] > numbers[i - 3] for i in range(3, len(numbers))])

print(part1)
print(part2)
