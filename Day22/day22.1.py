from collections import Counter, deque


def play(a, b):
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            b.append(b.popleft())
            b.append(a.popleft())
        else:
            a.append(a.popleft())
            a.append(b.popleft())
    return b if len(b) else a


def score(x):
    return sum(i * j for i, j in zip(range(len(x), 0, -1), x))


def part1():
    p1, p2 = open("in.txt").read().strip().split("\n\n")
    p1 = deque(map(int, p1.strip().split("\n")[1:]))
    p2 = deque(map(int, p2.strip().split("\n")[1:]))
    print(score(play(p1, p2)))


part1()
