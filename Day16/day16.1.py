def part1():
    def prep_rule(rule_string):
        rule1, rule2 = rule_string.split(" or ")
        a, b = list(map(int, rule1.split("-")))
        c, d = list(map(int, rule2.split("-")))
        return lambda x: (a <= x <= b) or (c <= x <= d)

    rules = []
    blocks = open("in.txt").read().split("\n\n")

    for line in blocks[0].split("\n"):
        rule_string = line.split(":")[1].strip()
        rules.append(prep_rule(rule_string))
    error = 0
    for line in blocks[2].split("\n")[1:]:
        x = list(map(int, line.strip().split(",")))
        for num in x:
            for rule in rules:
                if rule(num) is True:
                    break
            else:  # no-break
                # num does not satisfy _any_ rule
                # Hence this ticket is invalid
                error += num
    print(error)


part1()
