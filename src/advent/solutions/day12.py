from functools import lru_cache

from tqdm.cli import tqdm


def _parse_file(input_file: str) -> list[tuple[str, list[int]]]:
    out = []
    with open(input_file, "rt") as inf:
        for line in inf:
            line = line.strip()
            l, r = line.split(" ")
            nums = list(map(int, r.split(",")))
            out.append((l, nums))
    return out


@lru_cache()
def rec(l, remains):
    if not remains:
        if all(x in "?." for x in l):
            return 1
        return 0

    total = 0
    for i in range(len(l)):
        if i + remains[0] > len(l):
            break

        if all(x in "#?" for x in l[i : i + remains[0]]):
            if i + remains[0] == len(l) or l[i + remains[0]] in ".?":
                total += rec(l[i + remains[0] + 1 :], remains[1:])

        if l[i] == "#":
            # Once one gets left behind we have to stop
            break

    return total


def part1(input_file: str):
    inp = _parse_file(input_file)
    total = 0
    for l, nums in inp:
        total += rec(l, tuple(nums))
    print(f"Part 1: {total}")


def part2(input_file: str):
    inp = _parse_file(input_file)
    total = 0
    for l, nums in tqdm(inp):
        total += rec("?".join(l for _ in range(5)), tuple(nums * 5))
    print(f"Part 2: {total}")
