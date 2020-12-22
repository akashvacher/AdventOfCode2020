from collections import deque


game_cache = {}


def play(a, b):
    # If this game has been played before, reuse the result
    if (tuple(a), tuple(b)) in game_cache:
        return game_cache[(tuple(a), tuple(b))]

    # preserve the original args by making their copies
    A, B = deque(a), deque(b)
    seen_rounds = set()

    # Play rounds until one player runs out of cards, or till we see a duplicate round
    while len(A) > 0 and len(B) > 0:
        # If this round has been seen before in this game - player 1 wins
        if (tuple(A), tuple(B)) in seen_rounds:
            return (False, A)
        else:
            seen_rounds.add((tuple(A), tuple(B)))
        x, y = int(A.popleft()), int(B.popleft())
        if x <= len(A) and y <= len(B):
            # We need a subgame to decide the winner
            b_won, _ = play(
                deque(list(A)[:x]),
                deque(list(B)[:y]),
            )
        else:
            b_won = x < y
        if b_won:
            B.append(y)
            B.append(x)
        else:
            A.append(x)
            A.append(y)
    result = (True, B) if len(B) else (False, A)
    game_cache[(tuple(a), tuple(b))] = result
    return game_cache[(tuple(a), tuple(b))]


def score(x):
    return sum(i * j for i, j in zip(range(len(x), 0, -1), x))


def part2():
    p1, p2 = open("in.txt").read().strip().split("\n\n")
    p1 = deque(map(int, p1.strip().split("\n")[1:]))
    p2 = deque(map(int, p2.strip().split("\n")[1:]))
    _, p = play(p1, p2)
    print(score(p))


part2()
