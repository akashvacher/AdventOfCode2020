def part1():
    with open("in.txt") as f:
        # Group's answer can be a set of all characters irrespective of which individual contributed the character
        group_answer_sets = [ set(c for c in i if c!='\n') for i in f.read().split('\n\n')]
    print(sum(len(answer) for answer in group_answer_sets))
    

part1()
