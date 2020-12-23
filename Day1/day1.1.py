def part1():
    seen = set()
    with open("in.txt") as f:
        for line in f:
            num = int(line)
            if (2020 - num) in seen:
                print((2020 - num) * num)
                return
            seen.add(num)


part1()
