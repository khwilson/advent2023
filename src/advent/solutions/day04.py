from collections import defaultdict


def _parse_file(input_file: str) -> list[tuple[set[int], set[int]]]:
    out = []
    with open(input_file, "rt") as inf:
        for line in inf:
            _, r = line.split(":")
            l, r = r.split("|")
            out.append(
                (
                    {int(x.strip()) for x in l.split(" ") if x.strip()},
                    {int(x.strip()) for x in r.split(" ") if x.strip()},
                )
            )
    return out


def _get_val(l: set[int], r: set[int]):
    return 1 << (len(l & r) - 1) if l & r else 0


def part1(input_file: str):
    vals = _parse_file(input_file)
    total = sum(_get_val(l, r) for l, r in vals)
    print(f"Part 1: {total}")


def part2(input_file: str):
    vals = _parse_file(input_file)
    values = [_get_val(l, r) for l, r in vals]

    counts = defaultdict(int)
    for i, (l, r) in enumerate(vals):
        counts[i] += 1
        for j in range(i + 1, i + 1 + len(l & r)):
            counts[j] += counts[i]

    total = sum(counts[i] for i in range(len(values)))
    print(f"Part 2: {total}")
