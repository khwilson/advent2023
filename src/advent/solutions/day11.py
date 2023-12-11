def _parse_file(input_file: str) -> tuple[list[tuple[int, int]], set[int], set[int]]:
    galaxy_locations = []
    num_rows = 0
    num_cols = 0
    with open(input_file, "rt") as inf:
        for i, line in enumerate(inf):
            line = line.strip()
            num_rows += 1
            num_cols = len(line)
            for j, x in enumerate(line):
                if x == "#":
                    galaxy_locations.append((i, j))

    empty_cols = set(range(num_cols)) - {j for _, j in galaxy_locations}
    empty_rows = set(range(num_rows)) - {i for i, _ in galaxy_locations}

    return galaxy_locations, empty_rows, empty_cols


def _get_answer(
    galaxy_locations: list[tuple[int, int]],
    empty_rows: set[int],
    empty_cols: set[int],
    extra_dist: int,
) -> int:
    total = 0
    for gal_num, (gal_i, gal_j) in enumerate(galaxy_locations):
        for other_gal_i, other_gal_j in galaxy_locations[gal_num + 1 :]:
            min_i = min(gal_i, other_gal_i)
            max_i = max(gal_i, other_gal_i)
            min_j = min(gal_j, other_gal_j)
            max_j = max(gal_j, other_gal_j)
            dist = max_i - min_i + max_j - min_j
            dist += (extra_dist - 1) * len(set(range(min_i, max_i)) & empty_rows)
            dist += (extra_dist - 1) * len(set(range(min_j, max_j)) & empty_cols)
            total += dist
    return total


def part1(input_file: str):
    total = _get_answer(*_parse_file(input_file), 2)
    print(f"Part 1: {total}")


def part2(input_file: str):
    total = _get_answer(*_parse_file(input_file), 1_000_000)
    print(f"Part 2: {total}")
