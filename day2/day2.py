# type: ignore
import sys
import itertools

ranges = []
with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
    for rng in f.read().strip().split(","):
        a, b = rng.split("-")
        ranges.append((int(a), int(b)))


def invalid_p1(num):
    if len(num) % 2 != 0:
        return False
    return num[: len(num) // 2] == num[len(num) // 2 :]


def invalid_p2(num):
    divisors = [div for div in range(1, len(num)) if len(num) % div == 0]
    for div in divisors:
        if len(set(itertools.batched(num, div))) == 1:
            return True
    return False

assert invalid_p2('12341234')
assert invalid_p2('123123123')
assert invalid_p2('1212121212')
assert invalid_p2('1111111')
assert invalid_p2('7979779797')

part1 = 0
part2 = 0
for a, b in ranges:
    for num in range(a, b + 1):
        if invalid_p1(str(num)):
            part1 += num
        if invalid_p2(str(num)):
            part2 += num

print("Part 1:", part1)
print("Part 2:", part2)
