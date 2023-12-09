import math
import operator
import re
from functools import reduce


def _parse_file(input_file: str) -> list[tuple[int, int]]:
    with open(input_file, "rt") as inf:
        times = list(map(int, re.split(r"\s+", next(inf).strip())[1:]))
        distances = list(map(int, re.split(r"\s+", next(inf).strip())[1:]))

    return list(zip(times, distances))


def _parse_file2(input_file: str) -> tuple[int, int]:
    with open(input_file, "rt") as inf:
        time = int("".join(re.split(r"\s+", next(inf).strip())[1:]))
        distance = int("".join(re.split(r"\s+", next(inf).strip())[1:]))

    return time, distance


def part1(input_file: str):
    tots = []
    for time, distance in _parse_file(input_file):
        tot = 0
        for l_time in range(time + 1):
            l_distance = (time - l_time) * l_time
            if l_distance > distance:
                tot += 1
        tots.append(tot)
    print(f"Part 1: {reduce(operator.__mul__, tots, 1)}")


def part2(input_file: str):
    time, distance = _parse_file2(input_file)
    l = -(-time - math.sqrt(time**2 - 4 * 1 * distance)) / 2
    r = -(-time + math.sqrt(time**2 - 4 * 1 * distance)) / 2
    print(f"Part 2: {int(l - r)}")
