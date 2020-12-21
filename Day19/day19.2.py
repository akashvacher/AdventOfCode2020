from pprint import pprint
from pyformlang.cfg import Production, Variable, Terminal, CFG
from time import time


def part2():
    rules, words = open("in.txt").read().split("\n\n")

    rules = rules.replace("8: 42", "8: 42 | 42 8")
    rules = rules.replace("11: 42 31", "11: 42 31 | 42 11 31")

    variables = set()
    productions = set()
    terminals = set()
    for line in rules.split("\n"):
        left, right = line.split(":")
        left = Variable(left)
        variables.add(left)
        for expression in right.split("|"):
            if '"' in expression:  # Terminal expression
                expression = expression.strip('" ')
                right = [Terminal(expression)]
                terminals.add(Terminal(expression))
                productions.add(Production(left, right))
            else:
                right = [Variable(token) for token in expression.strip().split()]
                productions.add(Production(left, right))

    cfg = CFG(variables, terminals, Variable("0"), productions)
    count = sum(map(lambda x: 1 if cfg.contains(x) else 0, words.split("\n")))
    print(count)


part2()