def part2():

    with open("in.txt") as f:
        _ = f.readline()
        buses = f.readline()
    buses_and_delay = [(int(b), d) for d, b in enumerate(buses.split(",")) if b != "x"]

    bus, delay = buses_and_delay[0]
    t = bus - delay  # By definiton, bus*1 is a multiple of (t+delay)
    increment = bus  # Safe increment value to increase t by
    for bus, delay in buses_and_delay[1:]:
        while (t + delay) % bus != 0:
            t += increment
        increment *= bus
    print(t)


part2()
