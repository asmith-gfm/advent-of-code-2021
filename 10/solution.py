openers_by_closer = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<',
}

closers_by_opener = {v: k for k, v in openers_by_closer.items()}

part1_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

part2_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def part1(input):
    stack = []
    corrupted = 0
    for char in input:
        if openers_by_closer.keys().__contains__(char):
            if len(stack) == 0:
                corrupted += part1_points[char]
                break
            pop = stack.pop()
            if pop != openers_by_closer[char]:
                corrupted += part1_points[char]
                break
        else:
            stack.append(char)
    return corrupted


def part2(input):
    stack = []
    score = 0
    for char in input:
        if openers_by_closer.keys().__contains__(char):
            stack.pop()
        else:
            stack.append(char)
    for i in range(0, len(stack)):
        closer = closers_by_opener[stack.pop()]
        score *= 5
        score += part2_points[closer]
    return score


with open('input', 'r') as f:
    part1_score = 0
    part2_scores = []
    for line in f.readlines():
        part1_result = part1(line)
        part1_score += part1_result
        if part1_result == 0:
            part2_scores.append(part2(line.replace("\n", "")))
    part2_scores.sort()
    print(part1_score)
    print(part2_scores[int(len(part2_scores) / 2)])
