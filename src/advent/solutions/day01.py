import re


def _parse_line(line: str, re_str: str) -> int:
    matches = re.finditer(re_str, line)
    digits = [
        int(x.group(1))
        if x.group(1).isdigit()
        else {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }[x.group(1)]
        for x in matches
    ]
    val = 10 * digits[0] + digits[-1]
    return val


def part1(input_file: str):
    total = 0
    with open(input_file, "rt") as inf:
        for line in inf:
            total += _parse_line(line, r"(?=(\d))")

    print(f"Part 1: {total}")


def part2(input_file: str):
    total = 0
    with open(input_file, "rt") as inf:
        for line in inf:
            total += _parse_line(
                line, r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
            )

    print(f"Part 2: {total}")
