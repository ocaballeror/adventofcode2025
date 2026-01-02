import sys
from collections import defaultdict


def read_input():
    start = None
    splitters = set()

    with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line):
                if char == "S":
                    start = x, y
                elif char == "^":
                    splitters.add((x, y))

    return start, splitters


def part1():
    start, splitters = read_input()
    end = max(y for x, y in splitters) + 1
    rays = {start}

    count = 0

    while rays:
        for beam in list(rays):
            rays.remove(beam)
            beamx, beamy = beam
            if beamy == end:
                continue

            if (beamx, beamy + 1) in splitters:
                count += 1
                rays.add((beamx - 1, beamy + 1))
                rays.add((beamx + 1, beamy + 1))
            else:
                rays.add((beamx, beamy + 1))


    return count


def part2():
    start, splitters = read_input()
    end = max(y for x, y in splitters) + 1
    timelines = defaultdict(int)
    timelines[start] = 1

    total = 0

    while timelines:
        for particle, count in list(timelines.items()):
            particlex, particley = particle
            if particley == end:
                total += count
            elif (particlex, particley + 1) in splitters:
                timelines[(particlex - 1, particley + 1)] += count
                timelines[(particlex + 1, particley + 1)] += count
            else:
                timelines[(particlex, particley + 1)] += count

            timelines.pop(particle)

    return total


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
