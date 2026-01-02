import itertools
import sys


def read_input():
    ranges = []
    ingredients = []

    with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            a, b = line.split("-")
            ranges.append((int(a), int(b)))

        for line in f:
            ingredients.append(int(line))

    return ranges, ingredients


def overlap_ranges(ranges):
    changed = True
    new_ranges = set(ranges)
    while changed:
        changed = False
        for first, second in itertools.pairwise(sorted(new_ranges)):
            assert first <= second

            a, b = first
            c, d = second

            if a <= c <= b or a <= c - 1 <= b:
                new_ranges.difference_update({first})
                new_ranges.difference_update({second})
                new_ranges.add((min(a, c), max(b, d)))
                changed = True

    return new_ranges


def part1():
    ranges, ingredients = read_input()
    fresh = sum(any(ing in range(a, b + 1) for a, b in ranges) for ing in ingredients)
    return fresh


def part2():
    ranges, _ = read_input()
    fresh = sum(b - a + 1 for a, b in overlap_ranges(ranges))
    return fresh


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
