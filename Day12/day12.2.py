def part2():
    def process(line, wx, wy, x, y):
        action, value = line[:1], int(line[1:])
        if action == "F":
            x += value * wx
            y += value * wy

        elif action == "R":
            while value >= 90:
                wx, wy = wy, -wx
                value -= 90
        elif action == "L":
            while value >= 90:
                wx, wy = -wy, wx
                value -= 90
        elif action == "E":
            wx += value
        elif action == "W":
            wx -= value
        elif action == "N":
            wy += value
        elif action == "S":
            wy -= value

        return wx, wy, x, y

    wx, wy, x, y = 10, 1, 0, 0
    with open("in.txt") as f:
        for line in f:
            wx, wy, x, y = process(line, wx, wy, x, y)
    print(abs(x) + abs(y))


part2()
