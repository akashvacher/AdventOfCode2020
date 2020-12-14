import math


def part1():
    d = {}

    def apply_mask(mask, value):
        or_mask = int(mask.replace("X", "0"), 2)
        and_mask = int(mask.replace("X", "1"), 2)
        return (value | or_mask) & and_mask

    def process(line, mask):
        if "mask" in line:
            mask = line.split()[-1]
        else:
            address, _, value = line.split(" ")
            address = int(address.split("[")[-1].strip("]"))
            value = int(value)
            d[address] = apply_mask(mask, value)
        return mask

    mask = None
    with open("in.txt") as f:
        for line in f:
            line = line.strip()
            mask = process(line, mask)
    print(sum(d.values()))


part1()
