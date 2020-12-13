from collections import Counter


def part1():
    def get_neighbours(r, c, grid):
        R, C = len(grid), len(grid[0])
        n = [
            (r, c + 1),
            (r, c - 1),
            (r + 1, c),
            (r + 1, c + 1),
            (r + 1, c - 1),
            (r - 1, c),
            (r - 1, c + 1),
            (r - 1, c - 1),
        ]
        return Counter(
            [
                grid[i][j]
                for i, j in n
                if 0 <= i < R and 0 <= j < C and grid[i][j] != "."
            ]
        )

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
                elif cell == "#" and n["#"] >= 4:
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


part1()
