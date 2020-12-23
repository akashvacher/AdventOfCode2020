def part1():
    cups = list(map(int, open("in.txt").read().strip()))
    max_cup = max(cups)

    def tick(cups):
        # Extract the 3 cups after the current cup
        three_cups = cups[1:4]
        cups = cups[:1] + cups[4:]
        destination = (cups[0] - 1) or max_cup
        while destination in three_cups:
            destination = (destination - 1) or max_cup
        index = cups.index(destination)
        cups = cups[: index + 1] + three_cups + cups[index + 1 :]
        # Rotate cups so that cups array always has 0th element as the current cup
        cups = cups[1:] + cups[:1]
        return cups

    for _ in range(100):
        cups = tick(cups)
    index = cups.index(1)
    print("".join(str(i) for i in cups[index + 1 :] + cups[:index]))


part1()
