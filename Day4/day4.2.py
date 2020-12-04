def is_invalid_field(field, v):
    switch = {
        'byr': v.isnumeric() and 1920 <= int(v) <= 2002,
        'iyr': v.isnumeric() and 2010 <= int(v) <= 2020,
        'eyr': v.isnumeric() and 2020 <= int(v) <= 2030,
        'hgt': v[:-2].isnumeric() and ((v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193) or (v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76)),
        'hcl': v[0] == '#' and (v[1:].isnumeric() or (v[1:].isalnum() and v[1:].islower())),
        'ecl': v in ('amb blu brn gry grn hzl oth'.split()),
        'pid': len(v) == 9 and v.isnumeric(),
        'cid': True
    }
    return not switch[field]


def check_validity(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not all(field in passport for field in fields):
        # Clearly an invalid passport
        return False
    if any(is_invalid_field(field, value) for field, value in passport.items()):
        return False
    return True


def part2():
    passports = 0
    buffer = {}
    with open("in.txt") as f:
        for line in f:
            if len(line.strip()) == 0:
                # We have full details in buffer now
                # Check if it is a valid passport and then count it
                if check_validity(buffer):
                    passports += 1
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


part2()
