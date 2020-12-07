def part1():
    m = {}

    def parse_line(line):
        # Example lines:
        # faded blue bags contain no other bags.
        # light red bags contain 1 bright white bag, 2 muted yellow bags.
        line = line.strip('.')
        bag, contents = line.split(' bags contain ')
        contents = contents.replace(
            ' bags', '').replace(' bag', '').split(', ')
        # print(bag, contents)
        if contents[0] == 'no other':
            contents = {}
        contents = {' '.join(i.split()[1:]): int(i.split()[0]) for i in contents}
        # print(bag, contents)
        m[bag] = contents

    def contains_gold(color):
        # Returns the boolean answer to "Does this given bag contain a 'shiny gold' bag?"
        contents = m[color]
        if contents == {}:
            return False
        if 'shiny gold' in contents:
            return True
        return any(contains_gold(i) for i in contents)

    with open("in.txt") as f:
        for line in f:
            parse_line(line.strip())

    print(sum(1 for color in m if contains_gold(color)))


part1()
