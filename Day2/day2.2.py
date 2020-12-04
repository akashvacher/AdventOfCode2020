from collections import Counter


def part1():
    valid_rules = 0
    with open("in.txt") as f:
        for line in f:
            rule, string = (i.strip() for i in line.split(":"))
            rule, ch = rule.split()
            i1, i2 = (int(i) - 1 for i in rule.split('-'))
            if string[i1] == ch or string[i2] == ch:
                # Exactly one of these indices should have the characater
                if string[i1] == string[i2]:
                    # Password is invalid
                    continue
                valid_rules += 1
    print(valid_rules)


part1()
