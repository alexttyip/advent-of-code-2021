ints = open("input.txt", "r").readline().strip().split(",")

part1_days = 80
part2_days = 256

nums = {i: ints.count(f"{i}") for i in range(9)}

for i in range(part2_days):
    new_fish = nums[0]

    nums = {j: nums[j + 1] for j in range(8)}

    nums[6] += new_fish
    nums[8] = new_fish

    if i == part1_days - 1:
        print(sum(nums.values()))

print(sum(nums.values()))
