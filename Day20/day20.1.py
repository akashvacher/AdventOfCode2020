from collections import Counter
import math


def part1():
    def left(tile):
        return "".join(tile[r][0] for r in range(len(tile)))

    def right(tile):
        return "".join(tile[r][-1] for r in range(len(tile)))

    def canonicalize(x):
        return min(x, x[::-1])

    blocks = open("in.txt").read().split("\n\n")
    frequency = Counter()
    tiles = {}
    for block in blocks:
        tile_id, *tile = block.strip().split("\n")
        tile_id = int(tile_id.strip(":").split()[1])
        tiles[tile_id] = tile
        edges = list(map(canonicalize, [tile[0], tile[-1], left(tile), right(tile)]))
        frequency += Counter(edges)

    corners = []
    for tile_id, tile in tiles.items():
        edges = list(map(canonicalize, [tile[0], tile[-1], left(tile), right(tile)]))
        if sum(1 for edge in edges if frequency[edge] == 1) == 2:
            corners.append(tile_id)
    # print(corners)
    print(math.prod(corners))


part1()
