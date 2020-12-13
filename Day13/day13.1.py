import math


def part1():
    with open("in.txt") as f:
        start = int(f.readline())
        bus_ids = f.readline()
    bus_ids = [int(i) for i in bus_ids.split(",") if i != "x"]
    m = None
    for bus_id in bus_ids:
        wait_time = (bus_id - (start % bus_id)) % bus_id
        m = m or (wait_time, bus_id)  # Initialise m if it is None
        m = min(m, (wait_time, bus_id))
    print(math.prod(m))


part1()
