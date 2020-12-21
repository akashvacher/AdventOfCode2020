from collections import Counter


def part2():
    monster = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   "
    monster = monster.split("\n")

    def check(pic, i, j):
        mr, mc = len(monster), len(monster[0])
        for I in range(mr):
            for J in range(mc):
                if monster[I][J] == "#":
                    if pic[I + i][J + j] != "#":
                        return False
        return True

    def count_monsters(pic):
        R, C = len(pic), len(pic[0])
        mr, mc = len(monster), len(monster[0])
        count = 0
        for i in range(R - mr):
            for j in range(C - mc):
                if check(pic, i, j):
                    count += 1
        return count

    def trim(tile):
        return [row[1:-1] for row in tile[1:-1]]

    def place_one_tile(tiles, mat):
        mat_items = mat.items()
        for xy, t in mat_items:
            # Assume that tile t is in cartesian plane with coordinates (x, y)
            x, y = xy
            done = False
            for tile in tiles:
                for v in get_variants(tile):
                    if right(t) == left(v):
                        mat[(x + 1, y)] = v
                        tiles.remove(tile)
                        done = True
                        break
                    if bottom(t) == top(v):
                        mat[(x, y - 1)] = v
                        tiles.remove(tile)
                        done = True
                        break
                    if left(t) == right(v):
                        mat[(x - 1, y)] = v
                        tiles.remove(tile)
                        done = True
                        break
                    if top(t) == bottom(v):
                        mat[(x, y + 1)] = v
                        tiles.remove(tile)
                        done = True
                        break
                if done:
                    break
            if done:
                break
        return tiles, mat

    # def print_tile(tile):
    #     print("\n".join(["".join(row) for row in tile]))
    #     print()

    # def mat_print(mat):
    #     for k, v in mat.items():
    #         print(k)
    #         print_tile(v)

    def left(tile):
        return "".join(tile[r][0] for r in range(len(tile)))

    def right(tile):
        return "".join(tile[r][-1] for r in range(len(tile)))

    def top(tile):
        return tile[0]

    def bottom(tile):
        return tile[-1]

    def flip(tile):
        # Flip the tile around a horiztal axis
        return tile[::-1]

    def rotate_left(tile):
        return tuple(
            "".join(tile[r][i] for r in range(len(tile)))
            for i in range(-1, -len(tile[0]) - 1, -1)
        )

    def get_variants(tile):
        tile = tuple(tile)
        variants = set()
        for _ in range(4):
            variants.add(tile)
            tile = rotate_left(tile)
        tile = flip(tile)
        for _ in range(4):
            variants.add(tile)
            tile = rotate_left(tile)
        return variants

    blocks = open("in.txt").read().split("\n\n")
    tiles = set()
    for block in blocks:
        _, *tile = block.strip().split("\n")
        tiles.add(tuple(tile))

    # Pick one tile to begin solving the puzzle
    tile = tiles.pop()
    mat = {(0, 0): tile}

    # Fill the mat with tiles one-by-one
    while tiles:
        tiles, mat = place_one_tile(tiles, mat)

    ## Assemble the picture
    min_x, max_x = min(i[0] for i in mat), max(i[0] for i in mat)
    min_y, max_y = min(i[1] for i in mat), max(i[1] for i in mat)
    pic = []
    # To pick the tiles from the mat in correct order (left to right, top to bottom)
    # We essentially need to pick tiles from positions (min_x, max_y) to (max_x, max_y)
    # before reducing the y-coordinate and repeating the picking process
    for y in range(max_y, min_y - 1, -1):
        row = []
        for x in range(min_x, max_x + 1):
            if row:
                # left to right tile stitching
                row = [i + j for i, j in zip(row, trim(mat[(x, y)]))]
            else:
                row = trim(mat[(x, y)])
        # top to bottom tile stitching
        pic = pic + row

    pic_hashes = Counter("".join(pic))["#"]
    monster_hashes = Counter("".join(monster))["#"]
    ans = pic_hashes

    # Check all variants of the picture for monsters
    for v in get_variants(pic):
        num_monsters = count_monsters(v)
        # print(f"Saw {num_monsters} monsters")
        ans = min(ans, pic_hashes - num_monsters * monster_hashes)
    print(ans)


part2()