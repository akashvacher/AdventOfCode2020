def check_validity(passport):
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    return all(field in passport for field in fields)


def part1():
    passports = 0
    buffer = {}
    with open("in.txt") as f:
        for line in f:
            if len(line.strip()) == 0:
                # We have full details in buffer now
                # Check if it is a valid passport and then count it
                if check_validity(buffer):
                    passports+=1
                # Reset the buffer now
                buffer = {}
                continue
            # Read the line's fields and add them to buffer
            fields = line.strip().split()
            for field in fields:
                k, v = field.split(':')
                buffer[k] = v
    # For the last buffer, there is no terminating blank line, but we still need to check it
    if check_validity(buffer):
        passports += 1
    print(passports)
            

part1()
