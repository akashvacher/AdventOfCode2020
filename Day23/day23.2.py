def part2():
    max_cup = 1000000
    rounds = 10000000

    def tick(current, d):
        destination = (current - 1) or max_cup
        a = d[current]
        b = d[a]
        c = d[b]
        # Stitch this gap of 3 elements
        d[current] = d[c]
        while destination in (a, b, c):
            destination = (destination - 1) or max_cup
        d[c] = d[destination]
        d[destination] = a
        return d[current], d

    link = {}
    cups = list(map(int, open("in.txt").read().strip()))
    cups.extend(range(10, max_cup + 1))

    # Set up a circular linked list
    # A cup at index i points to the cup at index (i+1)%len(cups)
    for i, cup in enumerate(cups):
        link[cup] = cups[(i + 1) % len(cups)]

    current = cups[0]
    for _ in range(rounds):
        current, link = tick(current, link)
    a = link[1]
    b = link[a]
    print(a * b)


part2()
