import itertools
from collections import deque


def part2():
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

    def get_subarray_with_anomaly_sum(stream, anomaly):
        # Given the stream and anomaly, return the contiguous subarray of elements that sum up to the anomaly value
        low, high, L = 0, 1, len(stream)
        running_sum = sum(map(int, stream[low : high + 1]))

        while high < L:
            if running_sum == anomaly:
                return list(map(int, stream[low : high + 1]))
            if running_sum < anomaly:
                high += 1
                if high < L:
                    running_sum = running_sum + int(stream[high])
            if running_sum > anomaly:
                running_sum = running_sum - int(stream[low])
                low += 1
        print(f"No subarray found that sums up to anomaly value of {anomaly}")

    preamble_size = 25
    preamble = deque(stream[:preamble_size])
    # print(preamble)
    for i in stream[preamble_size:]:
        if is_possible(preamble, i):
            preamble.popleft()
            preamble.append(i)
        else:
            anomaly = int(i)
            break
    x = get_subarray_with_anomaly_sum(stream, anomaly)
    print(min(x) + max(x))


part2()
