moves = []
with open("input") as f:
    for line in f:
        moves.append(line.strip().replace("L", "-").replace("R", "+"))

head = 50
resets = 0
part1 = 0
part2 = 0
for move in moves:
    pre = head
    head = int(eval(f"{head}{move}"))
    while head < 0:
        head += 100
        if pre == 0:
            pre = 1
        else:
            part2 += 1
    while head > 100:
        head -= 100
        part2 += 1
    if head in (0, 100):
        part1 += 1
        part2 += 1
        head = 0

print('Part 1:', part1)
print('Part 2:', part2)
