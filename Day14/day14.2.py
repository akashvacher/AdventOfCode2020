import math


def part2():
    d = {}

    def all_possible_addresses(masked_address, prefix=None):
        # Given an masked address string (with 0s, 1s and Xs) and a prefix string depicting
        # how much of the masked address string has been decoded so far, return all the possible
        # versions of completely decoded address

        prefix = prefix or ""
        L = len(prefix)
        for i in masked_address[L:]:
            if i != "X":
                prefix += i
            else:
                x = all_possible_addresses(masked_address, prefix + "0")
                x.extend(all_possible_addresses(masked_address, prefix + "1"))
                return x
        return [prefix]

    def get_all_addresses(address, mask):
        # Given an address integer and a mask string, return
        # all the possible string addresses

        # Where mask has 1, overwrite with 1
        or_mask = int(mask.replace("X", "0"), 2)
        address = address | or_mask
        # Convert address into a string of 0s and 1s
        address = format(address, "b")
        # Add 0s to the left for padding
        address = "0" * (len(mask) - len(address)) + address
        # Incorporate Xs into the address string wherever needed as per the mask
        masked_address = "".join([i if j != "X" else j for i, j in zip(address, mask)])

        return all_possible_addresses(masked_address)

    def process(line, mask):
        if "mask" in line:
            mask = line.split()[-1]
        else:
            address, _, value = line.split(" ")
            address = int(address.split("[")[-1].strip("]"))
            value = int(value)
            for i in get_all_addresses(address, mask):
                d[i] = value
        return mask

    mask = None
    with open("in.txt") as f:
        for line in f:
            line = line.strip()
            mask = process(line, mask)
    print(sum(d.values()))


part2()
