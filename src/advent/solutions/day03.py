import itertools as its
import operator
import re
from collections import defaultdict
from functools import reduce


def _parse_file(
    input_file: str,
) -> tuple[dict[int, dict[int, str]], list[list[tuple[int, int]]]]:
    symbols: dict[int, dict[int, str]] = defaultdict(lambda: defaultdict(str))
    numbers: list[list[tuple[int, int]]] = []

    with open(input_file, "rt") as inf:
        num_row: list[tuple[int, int]] = []

        for i, line in enumerate(inf):
            line = line.strip()
            for m in re.finditer(r"(\d+)", line):
                num_row.append((m.start(1), int(m.group(1))))

            for m in re.finditer(r"([^.\d])", line):
                symbols[i][m.start(1)] = m.group(1)

            numbers.append(num_row)
            num_row = []
    return symbols, numbers


def part1(input_file: str):
    symbols, numbers = _parse_file(input_file)
    yes = 0
    for i, num_row in enumerate(numbers):
        for j, number in num_row:
            if any(
                symbols[ii][jj]
                for jj, ii in its.product(
                    range(j - 1, j + len(str(number)) + 1), range(i - 1, i + 2)
                )
            ):
                yes += number
    print(f"Part 1: {yes}")


def part2(input_file: str):
    symbols, numbers = _parse_file(input_file)

    gears: defaultdict[tuple[int, int], set[tuple[int, int, int]]] = defaultdict(set)
    for i, num_row in enumerate(numbers):
        for j, number in num_row:
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + len(str(number)) + 1):
                    if symbols[ii][jj] == "*":
                        gears[(ii, jj)].add((i, j, number))

    out = 0
    for v in gears.values():
        if len(v) == 2:
            out += reduce(operator.__mul__, (vvv[-1] for vvv in v), 1)

    print(f"Part 2: {out}")
