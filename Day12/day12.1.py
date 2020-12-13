def part1():
    directions = ["E", "S", "W", "N"]

    def process(line, facing, x, y):
        action, value = line[:1], int(line[1:])
        action = directions[facing] if action == "F" else action

        if action == "R":
            ticks = value // 90
            facing = (facing + ticks) % 4
        elif action == "L":
            ticks = value // 90
            facing = (facing - ticks) % 4
        elif action == "E":
            x += value
        elif action == "W":
            x -= value
        elif action == "N":
            y += value
        elif action == "S":
            y -= value

        return facing, x, y

    facing, x, y = 0, 0, 0
    with open("in.txt") as f:
        for line in f:
            # print(facing, x, y)
            facing, x, y = process(line, facing, x, y)
    print(abs(x) + abs(y))


part1()
