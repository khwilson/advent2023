import operator
import re
from collections import defaultdict
from functools import reduce
from itertools import cycle

from sympy import lcm


def _parse_file(input_file: str):
    outs = defaultdict(dict)
    with open(input_file, "rt") as inf:
        dirs = next(inf).strip()
        next(inf)
        for line in inf:
            s, l, r = re.findall(r"[A-Z]{3}", line.strip())
            outs[s]["L"] = l
            outs[s]["R"] = r
    return dirs, outs


def part1(input_file: str):
    dirs, outs = _parse_file(input_file)
    counter = 0
    pos = "AAA"
    i = cycle(dirs)
    while pos != "ZZZ":
        pos = outs[pos][next(i)]
        counter += 1
    print(f"Part 1: {counter}")


def part2(input_file: str):
    dirs, outs = _parse_file(input_file)
    a_pos = [x for x in outs if x[-1] == "A"]
    # Assert each node that ends in A only has one node that ends in Z on its cycle
    for pos in a_pos:
        i = cycle(dirs)
        ends = []
        while len(ends) < 2:
            if pos[-1] == "Z":
                ends.append(pos)
            pos = outs[pos][next(i)]
        assert len(ends) == 2
        assert ends[0] == ends[1]

    len_to_z = {}
    z_to_z = {}
    for pos in reversed(a_pos):
        i = cycle(dirs)
        counter = 0
        while pos[-1] != "Z":
            counter += 1
            pos = outs[pos][next(i)]
        len_to_z[pos] = counter

        counter = 0
        while counter == 0 or pos[-1] != "Z":
            counter += 1
            pos = outs[pos][next(i)]
        z_to_z[pos] = counter

    # Have they made life nice for us so we just need 0 mod all the numbers?
    assert all(len_to_z[key] == z_to_z[key] for key in len_to_z)

    # In which case, we just need to find the lcm of all the numers
    out = 1
    for v in len_to_z.values():
        out = lcm(out, v)
    print(f"Part 2: {out}")
