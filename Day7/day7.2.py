def part2():
    m = {}

    def parse_line(line):
        # Example lines:
        # faded blue bags contain no other bags.
        # light red bags contain 1 bright white bag, 2 muted yellow bags.
        line = line.strip(".")
        bag, contents = line.split(" bags contain ")
        contents = contents.replace(" bags", "").replace(" bag", "").split(", ")
        # print(bag, contents)
        if contents[0] == "no other":
            contents = {}
        contents = {" ".join(i.split()[1:]): int(i.split()[0]) for i in contents}
        # print(bag, contents)
        m[bag] = contents

    with open("in.txt") as f:
        for line in f:
            parse_line(line.strip())

    def num_inner_bags(color):
        # Given a bag color, return the total number of bags that are contained within it
        contents = m[color]
        if contents == {}:
            return 0
        return sum(count * (1 + num_inner_bags(bag)) for bag, count in contents.items())

    print(num_inner_bags("shiny gold"))


part2()
