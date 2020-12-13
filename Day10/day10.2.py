def part2():

    with open("in.txt") as f:
        adapters = list(sorted(map(int, f.read().split("\n"))))
    adapters = [0] + adapters + [adapters[-1] + 3]

    # Let ways[i] represent the ways to get adapters[i] jolts however way possible
    ways = [1]
    for i, adapter in enumerate(adapters):
        if i == 0:
            continue
        ways.append(0)
        j = i - 1
        while j >= 0 and adapter - adapters[j] <= 3:
            # With every possible pre-adapter within 3 jolt difference, the number of ways to use this current adapter increases
            ways[i] += ways[j]
            j -= 1
    # Number of ways to provide adapters[-1] jolts is in ways[-1]
    print(ways[-1])


part2()
