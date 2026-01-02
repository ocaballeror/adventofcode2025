import sys


def part1():
    with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
        ops = []
        for line in f:
            for idx, part in enumerate(line.split()):
                if idx >= len(ops):
                    ops.append([])
                ops[idx].append(part)

    total = 0
    for operation in ops:
        opcode = operation.pop(-1)
        total += eval(opcode.join(map(str, operation)))

    return total


def part2():
    with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
        ops = []
        for line in f:
            for idx, char in enumerate(line.removesuffix('\n')):
                if idx >= len(ops):
                    ops.append([])
                ops[idx].append(char)

    total = 0
    opcode = None
    parts = []
    for operation in ops:
        if operation[-1] in '+*':
            if opcode is not None:
                total += eval(opcode.join(parts))
                parts = []

            opcode = operation[-1]
            operation[-1] = ' '
        
        new = ''.join(operation).strip()
        if new:
            parts.append(new)

    total += eval(opcode.join(parts))

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
