def part1(bit_strings):
    frequency = []
    for i in range(0, len(bit_strings[0])):
        frequency.append({'0': 0, '1': 0})
    for s in bit_strings:
        for i in range(0, len(s)):
            frequency[i][s[i]] += 1
    bit_string = ""
    for position in frequency:
        bit_string += '0' if position['0'] > position['1'] else '1'
    gamma = int(bit_string, 2)
    epsilon = int(inverse(bit_string), 2)
    print(gamma * epsilon)


def part2(bit_strings):
    frequency = gather_frequency(bit_strings, 0)
    if len(frequency["0"]) < len(frequency["1"]):
        o2 = oxygen(frequency["1"], 1)
        co = co2(frequency["0"], 1)
    else:
        o2 = oxygen(frequency["0"], 1)
        co = co2(frequency["1"], 1)
    print(int(o2, 2) * int(co, 2))


def oxygen(bit_strings, position):
    if len(bit_strings) == 1:
        return bit_strings[0]
    frequency = gather_frequency(bit_strings, position)
    if len(frequency["0"]) > len(frequency["1"]):
        return oxygen(frequency["0"], position + 1)
    else:
        return oxygen(frequency["1"], position + 1)


def co2(bit_strings, position):
    if len(bit_strings) == 1:
        return bit_strings[0]
    frequency = gather_frequency(bit_strings, position)
    if len(frequency["0"]) > len(frequency["1"]):
        return co2(frequency["1"], position + 1)
    else:
        return co2(frequency["0"], position + 1)


def gather_frequency(bit_strings, position):
    frequency = {'0': [], '1': []}
    for s in bit_strings:
        frequency[s[position]].append(s)
    return frequency


def inverse(bit_string):
    return ''.join(['1' if i == '0' else '0' for i in bit_string])


# 3022 * 1073
with open('input', 'r') as f:
    bits = []
    for line in f.readlines():
        e = line.split()
        bits.append(e[0])
    # part1(bits)
    part2(bits)
