from collections import deque


game_cache = {}


def play(a, b):
    # If this game has been played before, reuse the result
    if (tuple(a), tuple(b)) in game_cache:
        return game_cache[(tuple(a), tuple(b))]

    # preserve the original inputs
    A, B = list(a), list(b)
    seen_rounds = set()

    # Play rounds until one player runs out of cards
    while len(a) > 0 and len(b) > 0:
        # If this round has been seen before in this game - player 1 wins
        if (tuple(a), tuple(b)) in seen_rounds:
            return (False, a)
        else:
            seen_rounds.add((tuple(a), tuple(b)))
        x, y = int(a.popleft()), int(b.popleft())
        if x <= len(a) and y <= len(b):
            # We need a subgame to decide the winner
            b_won, _ = play(
                deque(list(a)[:x]),
                deque(list(b)[:y]),
            )
        else:
            b_won = x < y
        if b_won:
            b.append(y)
            b.append(x)
        else:
            a.append(x)
            a.append(y)
    result = (True, b) if len(b) else (False, a)
    game_cache[(tuple(A), tuple(B))] = result
    return game_cache[(tuple(A), tuple(B))]


def score(x):
    return sum(i * j for i, j in zip(range(len(x), 0, -1), x))


def part2():
    p1, p2 = open("in.txt").read().strip().split("\n\n")
    p1 = deque(map(int, p1.strip().split("\n")[1:]))
    p2 = deque(map(int, p2.strip().split("\n")[1:]))
    _, p = play(p1, p2)
    print(score(p))


part2()
