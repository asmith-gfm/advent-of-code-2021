def part1(depths):
    counter = 0
    for pair in window(depths, 2):
        counter += is_increase(pair[0], pair[1])
    print(counter)


def part2(depths):
    counter = 0
    frames = window(depths, 3)
    for pair in window(frames, 2):
        counter += is_increase(sum(pair[0]), sum(pair[1]))
    print(counter)


def window(values, window_size):
    frames = []
    for i in range(len(values) - window_size + 1):
        frames.append(values[i: i + window_size])
    return frames


def is_increase(first, second):
    if first < second:
        return 1
    else:
        return 0


with open('input', 'r') as f:
    depths = []
    for line in f.readlines():
        depths.append(int(line))
    part1(depths)
    part2(depths)
