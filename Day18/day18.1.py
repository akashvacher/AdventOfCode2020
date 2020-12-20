def part1():
    def get_result(line):
        def apply(op, x, y):
            if op == "*":
                return x * y
            if op == "+":
                return x + y

        def resolve(a, b):
            if len(b) == 0:
                return a, b

            if b[-1] == ")":
                b.pop()
                x, y = [], []
                while b[-1] != "(":
                    y.append(b.pop())
                    x.append(a.pop())
                x.append(a.pop())
                while y:
                    x.append(apply(y.pop(), x.pop(), x.pop()))
                a.append(x[0])
                b.pop()
            return a, b

        a, b = [], []
        for i in "(" + line + ")":
            if i.isnumeric():
                a.append(int(i))
            else:
                b.append(i)
            a, b = resolve(a, b)
        return a.pop()

    result = 0
    with open("in.txt") as f:
        for line in f:
            result += get_result("".join(line.strip().split(" ")))
    print(result)


part1()
