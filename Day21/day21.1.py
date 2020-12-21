from collections import Counter


def part1():
    unfixed = {}
    fixed = {}
    freq = Counter()

    def refresh(unfixed, fixed):
        new_unfixed = {}
        for name, possible_codes in unfixed.items():
            x = possible_codes - set(fixed.values())
            if len(x) == 1:
                fixed[name] = x.pop()
            else:
                new_unfixed[name] = x
        if len(unfixed) != len(new_unfixed):
            # At least one name migrate from unfixed to fixed
            # Hence, we should refresh again
            return refresh(new_unfixed, fixed)
        return new_unfixed, fixed

    with open("in.txt") as f:
        for line in f:
            codes, names = line.replace("(", "").replace(")", "").split("contains")
            codes = codes.strip().split()
            names = names.strip().split(", ")
            freq += Counter(codes)
            for name in names:
                if name not in unfixed:
                    # Encountered this name for the first time
                    unfixed[name] = set(codes)
                else:
                    unfixed[name] = set(codes).intersection(unfixed[name])
                unfixed, fixed = refresh(unfixed, fixed)

    print(sum(count for code, count in freq.items() if code not in fixed.values()))


part1()
