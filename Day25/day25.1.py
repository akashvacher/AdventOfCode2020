def part1():
    def transform(subject):
        # Given a subject number, return an infinite stream of
        # transformed numbers with their associated loop sizes
        x, loop_size = 1, 1
        while True:
            x = (x * subject) % 20201227
            yield x, loop_size
            loop_size += 1

    p1, p2 = list(map(int, open("in.txt").read().strip().split("\n")))
    for a, loop_size_a in transform(7):
        if a == p1:
            break
    for b, loop_size_b in transform(7):
        if b == p2:
            break
    for x, y in transform(b):
        if y == loop_size_a:
            break
    print(x)


part1()
