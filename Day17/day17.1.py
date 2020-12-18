from collections import Counter


def part1():
    def create_state(grid):
        state = {}
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                state[(j, i, 0)] = cell
        return state

    def get_neighbours(x, y, z, grid):
        # For a given point (x,y,z) and the grid of all points
        # Return the counter for all neighbours of this point
        n = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if (dx, dy, dz) == (0, 0, 0):
                        # Exclude the point itself from neighbour list
                        continue
                    n.append((x + dx, y + dy, z + dz))
        return Counter(grid.get(point, ".") for point in n)

    def tick(old_state):
        new_state = {}
        min_x, max_x = min(i[0] for i in old_state), max(i[0] for i in old_state)
        min_y, max_y = min(i[1] for i in old_state), max(i[1] for i in old_state)
        min_z, max_z = min(i[2] for i in old_state), max(i[2] for i in old_state)

        # The new points of interest have x co-ordinates in [(min_x-1), (max_x+1)]
        # Similar ranges apply for the other dimensions too
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    neighbours = get_neighbours(x, y, z, old_state)
                    cell = old_state.get((x, y, z), ".")
                    if cell == "#":
                        if 2 <= neighbours["#"] <= 3:
                            new_state[(x, y, z)] = "#"
                    else:
                        if neighbours["#"] == 3:
                            new_state[(x, y, z)] = "#"
        return new_state

    x = open("in.txt").read().split("\n")
    state = create_state(x)
    for _ in range(6):
        # print(f"Doing tick={_} now")
        state = tick(state)
    print(sum(1 for i in state.values() if i == "#"))


part1()
