def part2():
    d = {}
    index = 1

    def get_next(last, d, index):
        if last not in d:
            d[last] = index
            return 0, d, index + 1
        diff = index - d[last]
        d[last] = index
        return diff, d, index + 1

    seed = list(map(int, open("in.txt").read().split(",")))
    for item in seed[:-1]:
        d[item] = index
        index += 1
    previous = seed[-1]
    while index < 30_000_000:
        previous, d, index = get_next(previous, d, index)
    print(previous)


part2()
