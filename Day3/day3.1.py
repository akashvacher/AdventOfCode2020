def part1():
    grid = []
    with open("in.txt") as f:
        for line in f:
            grid.append(line.strip())

    r, c = 0, 0
    R, C = len(grid), len(grid[0])
    trees = 0
    while r < R:
        if grid[r][c] == "#":
            trees += 1
        r += 1
        c = (c + 3) % C
    print(trees)


part1()
