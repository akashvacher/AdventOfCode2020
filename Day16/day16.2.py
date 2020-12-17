import math


def part2():
    def prep_rule(rule_string):
        rule1, rule2 = rule_string.split(" or ")
        a, b = list(map(int, rule1.split("-")))
        c, d = list(map(int, rule2.split("-")))
        return lambda x: (a <= x <= b) or (c <= x <= d)

    rules = {}
    blocks = open("in.txt").read().split("\n\n")
    for line in blocks[0].split("\n"):
        rule_name = line.split(":")[0].strip()
        rule_string = line.split(":")[1].strip()
        rules[rule_name] = prep_rule(rule_string)

    my_ticket = list(map(int, blocks[1].split("\n")[1].split(",")))

    tickets = []
    for line in blocks[2].split("\n")[1:]:
        x = list(map(int, line.strip().split(",")))
        is_valid = True
        for num in x:
            for rule in rules.values():
                if rule(num) is True:
                    break
            else:  # no-break
                # num does not satisfy _any_ rule
                # Hence this ticket is invalid
                is_valid = False
                break
        if is_valid:
            tickets.append(x)

    # Construct a dict field_to_rule_names mapping a field to all possible rule_names
    num_fields = len(tickets[0])
    field_to_rule_names = {k: list(rules.keys()) for k in range(num_fields)}
    for ticket in tickets:
        for field, value in enumerate(ticket):
            # From all plausible rules that may apply to this field,
            # keep only the ones that are valid for this value
            field_to_rule_names[field] = {
                rule_name
                for rule_name in field_to_rule_names[field]
                if rules[rule_name](value) is True
            }
    # For fields with exactly 1 rule_name mapped to them, let's keep them in fixed dict
    fixed = {
        field: rule_names
        for field, rule_names in field_to_rule_names.items()
        if len(rule_names) == 1
    }
    # Every other field can be stored in floating dict
    floating = {
        field: rule_names
        for field, rule_names in field_to_rule_names.items()
        if len(rule_names) > 1
    }

    while len(floating):
        fixed_rule_names = list(fixed.values())
        floating_fields = list(floating.keys())
        for rule_name in fixed_rule_names:
            rule_name = list(rule_name)[0]  # Get the rule_name string
            for i in floating_fields:
                if rule_name in floating[i]:
                    floating[i].remove(rule_name)
                if len(floating[i]) == 1:
                    # Migrate this field to fixed dict
                    fixed[i] = floating[i]
                    del floating[i]

    # fixed dict now is a map of items with each item as {integer:set of one string}
    # Let's reverse the mapping to be {string:integer} instead
    fixed = {list(rule_names)[0]: field for field, rule_names in fixed.items()}

    ans = math.prod(my_ticket[j] for i, j in fixed.items() if i.startswith("departure"))
    print(ans)


part2()
