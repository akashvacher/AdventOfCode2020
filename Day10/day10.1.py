def part1():

    with open("in.txt") as f:
        adapters = list(sorted(map(int, f.read().split("\n"))))
    adapters = [0] + adapters + [adapters[-1] + 3]
    d = {}
    for i, j in enumerate(adapters):
        if i == len(adapters) - 1:
            continue
        diff = adapters[i + 1] - j
        d[diff] = d.get(diff, 0) + 1
    print(d.get(1, 1) * d.get(3, 1))


part1()
