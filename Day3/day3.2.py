import math


def count_trees_for_slope(grid, slope):
    column_increment, row_increment = slope
    r, c = 0, 0
    R, C = len(grid), len(grid[0])
    trees = 0
    while r < R:
        if grid[r][c] == "#":
            trees += 1
        r += row_increment
        c = (c + column_increment) % C
    return trees


def part2():
    grid = []
    with open("in.txt") as f:
        for line in f:
            grid.append(line.strip())
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(math.prod(count_trees_for_slope(grid, slope) for slope in slopes))


part2()
