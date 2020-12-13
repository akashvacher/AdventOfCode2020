def part1():
    with open("in.txt") as f:
        start = int(f.readline())
        buses = f.readline()
    buses = [int(i) for i in buses.split(",") if i != "x"]
    m = None
    for bus in buses:
        wait_time = (bus - (start % bus)) % bus
        m = m or (wait_time, bus)  # Initialise m if it is None
        m = min(m, (wait_time, bus))
    print(m[0] * m[1])


part1()
