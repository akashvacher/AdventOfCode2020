def part1():
    program = []
    with open("in.txt") as f:
        for line in f:
            program.append(line.strip())

    def run_instruction(program, index, acc):
        # Given a program, index and accumulator, return the new index and accumulator values after running the given instruction

        instruction, val = program[index].split()
        val = int(val)
        if instruction == "nop":
            return index + 1, acc
        if instruction == "acc":
            return index + 1, acc + val
        if instruction == "jmp":
            return index + val, acc

    # instrction pointer and accumulator
    ip, acc = 0, 0
    # set of already visited instructions
    visited = set()
    while ip not in visited:
        visited.add(ip)
        ip, acc = run_instruction(program, ip, acc)
    else:  # no-break
        print(acc)


part1()
