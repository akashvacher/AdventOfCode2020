from pprint import pprint
from collections import Counter


def part2():
    def get_colored_neighbors(tile, state):
        x, y = tile
        return Counter(
            [
                state.get((x + 2, y), 0),
                state.get((x + 1, y + 1), 0),
                state.get((x - 1, y + 1), 0),
                state.get((x - 2, y), 0),
                state.get((x - 1, y - 1), 0),
                state.get((x + 1, y - 1), 0),
            ]
        )[1]

    def get_border(state):
        border = []
        for x, y in state.keys():
            around = [
                (x + 2, y),
                (x + 1, y + 1),
                (x - 1, y + 1),
                (x - 2, y),
                (x - 1, y - 1),
                (x + 1, y - 1),
            ]
            border.extend([i for i in around if i not in state])
        return border

    def tick(state):
        new_state = {}
        border = get_border(state)

        for tile in list(state.keys()) + border:
            color = state.get(tile, 0)
            n = get_colored_neighbors(tile, state)
            if color == 1 and (n == 0 or n > 2):
                new_state[tile] = 0
            elif color == 0 and n == 2:
                new_state[tile] = 1
            else:
                new_state[tile] = color
        return new_state

    def flip_tile(line, state):
        d = []
        line = iter(line)
        for i in line:
            if i in ("s", "n"):
                j = next(line)
                d.append(i + j)
            else:
                d.append(i)
        d = Counter(d)
        x = 2 * d["e"] + d["ne"] + d["se"] - 2 * d["w"] - d["nw"] - d["sw"]
        y = d["ne"] + d["nw"] - d["se"] - d["sw"]
        tile = (x, y)
        # Flip the state of tile from 0 to 1 and vice-versa
        # if it's a new tile, it's assumed to be white (denoted by 0)
        state[tile] = state.get(tile, 0) ^ 1
        return state

    state = {}
    with open("in.txt") as f:
        for line in f:
            state = flip_tile(line.strip(), state)

    for _ in range(100):
        state = tick(state)
    print(sum(state.values()))


part2()
