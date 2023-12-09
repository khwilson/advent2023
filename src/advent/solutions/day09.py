def _parse_file(input_file: str) -> list[list[int]]:
    lines = []
    with open(input_file, "rt") as inf:
        for line in inf:
            line = line.strip()
            lines.append([int(v) for v in line.split(" ")])
    return lines


def _embiggen(line: list[int]) -> list[list[int]]:
    embiggen = [line]
    while not all(x == 0 for x in embiggen[-1]):
        next_line = [r - l for l, r in zip(embiggen[-1], embiggen[-1][1:])]
        embiggen.append(next_line)
    return embiggen


def part1(input_file: str):
    data = _parse_file(input_file)
    total = 0
    for line in data:
        embiggen = _embiggen(line)
        next_val = 0
        for line in reversed(embiggen[:-1]):
            next_val += line[-1]
        total += next_val
    print(f"Part 1: {total}")


def part2(input_file: str):
    data = _parse_file(input_file)
    total = 0
    for line in data:
        embiggen = _embiggen(line)
        next_val = 0
        for line in reversed(embiggen[:-1]):
            next_val = line[0] - next_val
        total += next_val
    print(f"Part 2: {total}")
