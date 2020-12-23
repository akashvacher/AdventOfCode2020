from collections import Counter


def part1():
    valid_rules = 0
    with open("in.txt") as f:
        for line in f:
            rule, string = (i.strip() for i in line.split(":"))
            rule, ch = rule.split()
            min_count, max_count = (int(i) for i in rule.split("-"))
            count = Counter(string)
            if min_count <= count[ch] <= max_count:
                valid_rules += 1
    print(valid_rules)


part1()
