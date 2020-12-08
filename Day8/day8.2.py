import sys


def part2():
    program = []
    with open("in.txt") as f:
        for line in f:
            program.append(line.strip())
    # Append a custom instruction to the program to signify end of execution has been reached
    program.append("end +0")

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
        if instruction == "end":
            return None, acc

    def try_running(program):
        # Run the given program. Return None if the program gets stuck in an infinite loop.
        # If the supplied program terminates, print the accumulator value and exit

        # instrction pointer and accumulator
        ip, acc = 0, 0
        # set of already visited instructions
        visited = set()
        while ip is not None and ip not in visited:
            visited.add(ip)
            ip, acc = run_instruction(program, ip, acc)
        if ip is None:
            # Program terminated successfully!
            print(acc)
            sys.exit(1)

    i = len(program) - 1
    while i >= 0:
        if "nop" in program[i]:
            program[i] = program[i].replace("nop", "jmp")
            try_running(program)
            program[i] = program[i].replace("jmp", "nop")
        elif "jmp" in program[i]:
            program[i] = program[i].replace("jmp", "nop")
            try_running(program)
            program[i] = program[i].replace("nop", "jmp")
        i = i - 1


part2()
