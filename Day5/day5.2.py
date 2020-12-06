def get_id(boarding_pass):
    boarding_pass = ''.join(['0' if i in 'FL' else '1' for i in boarding_pass])
    r, c = boarding_pass[:7], boarding_pass[7:]
    return int(r, 2)*8 + int(c, 2)


def part2():
    s = set()
    with open("in.txt") as f:
        for line in f:
            s.add(get_id(line.strip()))
    low, high = min(s), max(s)
    for i in range(low, high):
        if i not in s:
            print(i)
            break


part2()
