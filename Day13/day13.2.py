from math import gcd


def part2():
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    with open("in.txt") as f:
        _ = f.readline()
        bus_ids = f.readline()
    bus_ids_and_delay = [
        (int(bus_id), delay)
        for delay, bus_id in enumerate(bus_ids.split(","))
        if bus_id != "x"
    ]

    bus_id, delay = bus_ids_and_delay[0]
    t = bus_id - delay  # This t is suitable as bus_id*1 is a multiple of (t+delay)
    increment = bus_id  # Safe increment value to increase t with
    for bus_id, delay in bus_ids_and_delay[1:]:
        # Find the next value of t which is suitable for this bus_id
        # by repeatedly incrementing it
        while (t + delay) % bus_id != 0:
            t += increment
        # The new safe increment value has to be a multiple of this bus_id
        # AND maintain that it is a multiple of all the bus_ids that came before this one
        # Hence, we take the LCM of this bus_id with existing increment to get the new increment
        increment = lcm(increment, bus_id)
    print(t)


part2()
