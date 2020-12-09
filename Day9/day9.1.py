import itertools
from collections import deque


def part1():
    stream = []
    with open("in.txt") as f:
        for line in f:
            stream.append(line.strip())

    def is_possible(previous_items, item):
        # Returns the boolean answer to the query "can the given item occur in the stream after the given list of previous items?"
        for i in itertools.combinations(previous_items, 2):
            if sum(map(int, i)) == int(item):
                return True
        return False

    preamble_size = 25
    preamble = deque(stream[:preamble_size])
    # print(preamble)
    for i in stream[preamble_size:]:
        if is_possible(preamble, i):
            preamble.popleft()
            preamble.append(i)
        else:
            print(i)
            break


part1()
