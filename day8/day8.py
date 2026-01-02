import itertools
import math
import sys


def read_input():
    boxes = []
    with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
        for line in f:
            boxes.append(tuple(map(int, line.split(","))))

    return boxes


def compute_distances(boxes):
    distances = {}
    for one, other in itertools.combinations(boxes, r=2):
        distances[(one, other)] = math.sqrt(
            (one[0] - other[0]) ** 2
            + (one[1] - other[1]) ** 2
            + (one[2] - other[2]) ** 2
        )

    return distances


def simulate(boxes):
    groups = []
    group_map = {}

    distances = compute_distances(boxes)
    for one, other in sorted(distances, key=lambda x: distances[x]):
        if one in group_map and other in group_map:
            first = group_map[one]
            second = group_map[other]
            if first != second:
                groups[first].extend(groups[second])

                for box, boxgroup in group_map.items():
                    if boxgroup == second:
                        group_map[box] = first
                groups[second] = []
        elif one in group_map:
            groups[group_map[one]].append(other)
            group_map[other] = group_map[one]
        elif other in group_map:
            groups[group_map[other]].append(one)
            group_map[one] = group_map[other]
        else:
            groups.append([one, other])
            group_map[one] = len(groups) - 1
            group_map[other] = len(groups) - 1

        yield one, other, groups


def part1():
    boxes = read_input()
    cables = 1000 if len(sys.argv) == 1 or sys.argv[1] == "input" else 10
    for _, _, groups in simulate(boxes):
        cables -= 1
        if cables == 0:
            break

    sizes = sorted(map(len, groups))
    return sizes[-3] * sizes[-2] * sizes[-1]


def part2():
    boxes = read_input()

    for box1, box2, groups in simulate(boxes):
        if max(map(len, groups)) == len(boxes):
            return box1[0] * box2[0]


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
