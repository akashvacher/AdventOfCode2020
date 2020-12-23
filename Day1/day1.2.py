def part2():
    nums = []
    with open("in.txt") as f:
        for line in f:
            nums.append(int(line))
    for i, I in enumerate(nums):
        for j, J in enumerate(nums[i + 1 :]):
            for k, K in enumerate(nums[j + 1 :]):
                if I + J + K == 2020:
                    print(I * J * K)
                    return


part2()
