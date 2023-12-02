import operator
from collections import defaultdict
from functools import reduce


def _split_reveal(reveal: str) -> list[tuple[int, str]]:
    pairs = [pair.strip().split(" ") for pair in reveal.split(",")]
    return [(int(pair[0]), pair[1]) for pair in pairs]


def _parse_file(input_file: str) -> list[list[tuple[int, str]]]:
    out = []
    with open(input_file, "rt") as inf:
        for line in inf:
            out.append([_split_reveal(x) for x in line.strip().split(":")[1].split(";")])
    return out


def part1(input_file: str):
    maxes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total = 0
    all_reveals = _parse_file(input_file)
    for line_num, reveals in enumerate(all_reveals, 1):
        if any(y[0] > maxes[y[1]] for x in reveals for y in x):
            continue
        total += line_num
    print(f"Part 1: {total}")


def part2(input_file: str):
    total = 0
    all_reveals = _parse_file(input_file)
    for reveals in all_reveals:
        vals = defaultdict(int)
        for reveal in reveals:
            for num, name in reveal:
                vals[name] = max(vals[name], num)
        power = reduce(operator.__mul__, vals.values(), 1)
        total += power
    print(f"Part 2: {total}")
