def part2():
    a = []
    with open("in.txt") as f:
        for line in f:
            a.append(int(line))
    # print(a)
    for i, I in enumerate(a):
        for j, J in enumerate(a[i+1:]):
            for k, K in enumerate(a[j+1:]):
                if I+J+K == 2020:
                    print(I*J*K)
                    return
    print(f"Didn't find what you were looking for")


part2()
