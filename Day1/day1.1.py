def part1():
    s = set()
    with open("in.txt") as f:
        for line in f:
            num = int(line)
            if (2020-num) in s:
                print((2020-num)*num)
                return
            s.add(num)

    print(f"Didn't find what you were looking for")


part1()
