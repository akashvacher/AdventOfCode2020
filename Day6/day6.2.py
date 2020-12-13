def part2():
    with open("in.txt") as f:
        group_answers = [i for i in f.read().split("\n\n")]
    count = 0
    for group_answer in group_answers:
        # Let's split this single string into individual answers within the group, one set per person
        individual_answer_sets = [set(answer) for answer in group_answer.split("\n")]
        agreements = set.intersection(*individual_answer_sets)
        count += len(agreements)
    print(count)


part2()
