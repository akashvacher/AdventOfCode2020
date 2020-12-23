from collections import Counter


def part1():
    valid_rules = 0
    with open("in.txt") as f:
        for line in f:
            rule, string = (i.strip() for i in line.split(":"))
            rule, ch = rule.split()
            pos1, pos2 = (int(i) - 1 for i in rule.split("-"))
            if string[pos1] == ch or string[pos2] == ch:
                # Exactly one of these indices should have the characater
                if string[pos1] == string[pos2]:
                    # Password is invalid
                    continue
                valid_rules += 1
    print(valid_rules)


part1()
