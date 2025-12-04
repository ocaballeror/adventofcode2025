import sys

banks = []
with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
    for line in f:
        banks.append(list(map(int, line.strip())))


def joltage(bank, count=2):
    parts = []
    while count > 0:
        highest = max(bank[: len(bank) - count + 1])
        idx = bank.index(highest)
        bank = bank[idx + 1 :]
        parts.append(highest)
        count -= 1

    return int("".join(map(str, parts)))


part1 = sum(joltage(bank, 2) for bank in banks)
part2 = sum(joltage(bank, 12) for bank in banks)


print("Part 1:", part1)
print("Part 2:", part2)
