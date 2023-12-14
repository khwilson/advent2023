import numpy as np
from tqdm.cli import tqdm


def _parse_file(input_file: str) -> list[list[str]]:
    lines = []
    with open(input_file, "rt") as inf:
        for line in inf:
            line = line.strip()
            lines.append([x for x in line])
    return lines


def _tilt_north(lines):
    for i, line in enumerate(lines):
        for j, elt in enumerate(line):
            if elt == "O":
                this_i = i
                while this_i >= 1:
                    this_i -= 1
                    if lines[this_i][j] == ".":
                        lines[this_i][j] = "O"
                        lines[this_i + 1][j] = "."
                    else:
                        break


def part1(input_file: str):
    lines = _parse_file(input_file)
    _tilt_north(lines)

    total = 0
    for i, line in enumerate(reversed(lines), 1):
        total += i * sum(1 for x in line if x == "O")
    print(f"Part 1: {total}")


def part2(input_file: str):
    lines = np.array(_parse_file(input_file))
    seen = {}
    num_rounds = 1_000_000_000
    for ii in tqdm(range(num_rounds)):
        for _ in range(4):
            _tilt_north(lines)
            lines = np.rot90(lines, k=-1)

        frozen = tuple(tuple(line) for line in lines)

        if frozen in seen:
            num_rounds = ((num_rounds - seen[frozen]) % (ii - seen[frozen])) - 1
            break
        else:
            seen[frozen] = ii

    for ii in range(num_rounds):
        for _ in range(4):
            _tilt_north(lines)
            lines = np.rot90(lines, k=-1)

    total = 0
    for i, line in enumerate(reversed(lines), 1):
        total += i * sum(1 for x in line if x == "O")
    print(f"Part 2: {total}")
