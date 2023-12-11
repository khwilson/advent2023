def _parse_file(input_file: str):
    mappings = []
    with open(input_file, "rt") as inf:
        seed_line = next(inf).strip()
        seeds = [int(y) for x in seed_line.split(":")[1].split(" ") if (y := x.strip())]
        next(inf)

        this_mapping = []
        first_line = True
        for line in inf:
            if first_line:
                first_line = False
                continue
            line = line.strip()
            if not line:
                mappings.append(this_mapping)
                this_mapping = []
                first_line = True
                continue
            this_mapping.append(list(map(int, line.split(" "))))

        mappings.append(this_mapping)

    return seeds, mappings


def part1(input_file: str):
    seeds, mappings = _parse_file(input_file)
    locs = []
    for seed in seeds:
        pos = seed
        for mapping in mappings:
            found = False
            for d_start, s_start, l in mapping:
                if s_start <= pos < s_start + l:
                    pos = d_start + (pos - s_start)
                    found = True
                    break
            if not found:
                pos = pos
        locs.append(pos)

    print(f"Part 1: {min(locs)}")


def foo(
    start, end, other_start, dest, other_end
) -> tuple[list[tuple[int, int]], tuple[int, int] | None]:
    def fix(l, r) -> tuple[int, int]:
        return l - other_start + dest, r - other_start + dest

    if start <= other_start <= other_end <= end:
        return [(start, other_start), (other_end, end)], fix(other_start, other_end)

    if other_start <= start <= other_end <= end:
        return [(other_end, end)], fix(start, other_end)

    if start <= other_start <= end <= other_end:
        return [(start, other_start)], fix(other_start, end)

    if other_start <= start <= end <= other_end:
        return [], fix(start, end)

    if (end <= other_start) or (other_end <= start):
        return [(start, end)], None

    assert False


def part2(input_file: str):
    seeds, mappings = _parse_file(input_file)
    intervals = [
        (l_seed, l_seed + len_seed) for l_seed, len_seed in zip(seeds[::2], seeds[1::2])
    ]
    for mapping in mappings:
        new_intervals = []

        for start, end in intervals:
            next_intervals = [(start, end)]
            for d_start, s_start, l in mapping:
                new_next_intervals = []
                for n_start, n_end in next_intervals:
                    bar, mapped_interval = foo(
                        n_start, n_end, s_start, d_start, s_start + l
                    )
                    new_next_intervals.extend(bar)
                    if mapped_interval:
                        new_intervals.append(mapped_interval)
                next_intervals = new_next_intervals
            new_intervals.extend(next_intervals)
        intervals = new_intervals
    min_loc = min(l for l, r in intervals if l < r)
    print(f"Part 2: {min_loc}")
