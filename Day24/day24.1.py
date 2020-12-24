from pprint import pprint
from collections import Counter


def part1():
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

    print(sum(state.values()))


part1()
