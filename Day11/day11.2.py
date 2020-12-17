from collections import Counter


def part2():
    def is_valid(r, c, grid):
        R, C = len(grid), len(grid[0])
        return 0 <= r < R and 0 <= c < C

    def get_neighbours(r, c, grid):
        n = []

        def include(inc_r, inc_c, n, grid):
            x, y = r + inc_r, c + inc_c
            while is_valid(x, y, grid):
                if grid[x][y] != ".":
                    n.append(grid[x][y])
                    break
                else:
                    x, y = x + inc_r, y + inc_c
            return n

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx, dy) == (0, 0):
                    continue
                n = include(dx, dy, n, grid)
        return Counter(n)

    def tick(grid):
        G = [[0] * len(grid[0]) for i in range(len(grid))]
        for r, R in enumerate(grid):
            for c, cell in enumerate(R):
                if cell == ".":
                    G[r][c] = "."
                    continue
                n = get_neighbours(r, c, grid)
                # print(f"Neighbours of {r},{c} --> {n}")
                if cell == "L" and n["#"] == 0:
                    G[r][c] = "#"
                elif cell == "#" and n["#"] >= 5:
                    G[r][c] = "L"
                else:
                    G[r][c] = cell
        return G

    grid = []
    with open("in.txt") as f:
        for line in f:
            grid.append(list(line.strip()))

    prev = None
    while prev != grid:
        # print()
        # for r in grid:
        #     print("".join(r))
        prev, grid = grid, tick(grid)

    print(sum(sum(1 for cell in row if cell == "#") for row in grid))


part2()
