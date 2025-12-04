import sys

grid = {}

with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            grid[x, y] = char

def adjacent(pos):
    x, y = pos
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for dirx, diry in dirs:
        other = x + dirx, y + diry
        if other in grid:
            yield other


def removable():
    rolls = []
    for pos, char in grid.items():
        if char != '@':
            continue
        if sum(grid[other] == '@' for other in adjacent(pos)) < 4:
            rolls.append(pos)
    return rolls


part1 = len(removable())

part2 = 0
while True:
    to_remove = removable()
    if not to_remove:
        break

    for roll in to_remove:
        part2 += 1
        grid[roll] = '.'

print('Part 1:', part1)
print('Part 2:', part2)
