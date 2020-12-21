from pprint import pprint
import re


def check(x, pattern):
    return True if re.compile("^" + pattern + "$").match(x) else False


def helper(solved, unsolved, target="0"):
    if target in solved:
        return solved[target]

    lhs, rhs = target, unsolved[target]
    string = []
    # For every epression 'e' in RHS
    for e in rhs:
        e_str = ""
        # For every token in the expression 'e'
        for token in e:
            # Resolve token to a string
            token_str = helper(solved, unsolved, target=token)
            # Resolve 'e' to a string
            e_str += "(" + token_str + ")"
        string.append(e_str)

    # Resolve RHS to a string
    string = "|".join(string)

    # Migrate this target over from unsolved to solved
    solved[lhs] = string
    del unsolved[lhs]

    # Finally, return the regex pattern string for target
    return solved[target]


def get_rule(line):
    is_terminal = False
    left, right = line.split(":")
    if '"' in right:
        right = [[right.strip('" ')]]
        is_terminal = True
    else:
        right = [i.strip().split() for i in right.split("|")]
    return left, right, is_terminal


def part1():
    terminals, non_terminals = {}, {}
    rules, words = open("in.txt").read().split("\n\n")
    for line in rules.split("\n"):
        left, right, is_terminal = get_rule(line.strip())
        if is_terminal:
            terminals[left] = right[0][0]
        else:
            non_terminals[left] = right

    pattern = helper(terminals, non_terminals)
    count = 0
    for line in words.split("\n"):
        if check(line.strip(), pattern):
            count += 1
    print(count)


part1()
