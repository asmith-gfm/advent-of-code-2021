from submarine import Submarine, AimingSubmarine


def part1(instructions):
    sub = Submarine()
    for instruction in instructions:
        sub.drive(instruction[0], instruction[1])
    print(sub.depth * sub.distance)


def part2(instructions):
    sub = AimingSubmarine()
    for instruction in instructions:
        sub.drive(instruction[0], instruction[1])
    print(sub.depth * sub.distance)


with open('input', 'r') as f:
    instructions = []
    for line in f.readlines():
        e = line.split()
        instructions.append([e[0], int(e[1])])
    part1(instructions)
    part2(instructions)
