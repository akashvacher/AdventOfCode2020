def get_id(boarding_pass):
    boarding_pass = "".join(["0" if i in "FL" else "1" for i in boarding_pass])
    r, c = boarding_pass[:7], boarding_pass[7:]
    return int(r, 2) * 8 + int(c, 2)


def part1():
    m = None
    with open("in.txt") as f:
        for line in f:
            i = get_id(line.strip())
            m = m or i
            m = max(m, i)
    print(m)


part1()
