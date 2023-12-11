from collections import defaultdict, deque

GOES_LEFT = "-J7"
GOES_RIGHT = "-FL"
GOES_UP = "|JL"
GOES_DOWN = "|F7"


def _parse_file(
    input_file: str,
) -> tuple[int, dict[int, dict[int, list[tuple[int, int]]]], int, int]:
    # Just read in the input for easy parsing
    data: dict[int, dict[int, str]] = defaultdict(lambda: defaultdict(str))
    s_loc = (-1, -1)
    with open(input_file, "rt") as inf:
        for i, line in enumerate(inf):
            # Staring at my input, the S is actually a 7
            # Could do this programatically, but why?
            if "S" in line:
                s_loc = (i, line.index("S"))
            data[i].update(
                {j: x if x != "S" else "7" for j, x in enumerate(line.strip())}
            )

    num_rows = len(data)
    num_cols = len(data[0])

    graph: dict[int, dict[int, list[tuple[int, int]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for i in range(len(data)):
        for j in range(len(data[i])):
            nbd = []
            if data[i][j] in GOES_DOWN:
                if data[i + 1][j] in GOES_UP:
                    nbd.append((i + 1, j))
            if data[i][j] in GOES_UP:
                if data[i - 1][j] in GOES_DOWN:
                    nbd.append((i - 1, j))
            if data[i][j] in GOES_LEFT:
                if data[i][j - 1] in GOES_RIGHT:
                    nbd.append((i, j - 1))
            if data[i][j] in GOES_RIGHT:
                if data[i][j + 1] in GOES_LEFT:
                    nbd.append((i, j + 1))
            if len(nbd) == 2:
                graph[i][j] = nbd
    return s_loc, graph, num_rows, num_cols, data


def _get_dists(
    s_loc: tuple[int, int], graph: dict[int, dict[int, list[tuple[int, int]]]]
) -> dict[tuple[int, int], int]:
    seen: dict[tuple[int, int], int] = {}
    queue: deque[tuple[int, int, int]] = deque([(*s_loc, 0)])
    while queue:
        i, j, d = queue.popleft()
        for ii, jj in graph[i][j]:
            if (ii, jj) in seen and seen[(ii, jj)] <= d + 1:
                continue
            seen[(ii, jj)] = d + 1
            queue.append((ii, jj, d + 1))
    return seen


def part1(input_file: str):
    s_loc, graph, _, _, _ = _parse_file(input_file)
    seen = _get_dists(s_loc, graph)
    print(f"Part 1: {max(seen.values())}")


def part2(input_file: str):
    s_loc, graph, num_rows, num_cols, raw = _parse_file(input_file)

    # So I'm supposed to use the Jordan Curve Theorem, but it's
    # rather weird on the 2d plane. To think about it, imagine a line
    # going from left to right at the half integers. We choose that
    # F and 7 contain a | and that L and J do not. Thus, if we
    # cross F, 7, or |, we flip the parity. Otherwise, we do not

    tiles = set(_get_dists(s_loc, graph))  # Filter out junk
    total = 0

    # new_graph is just kept for debugging purposes. Keeps only
    # the true loop and marks tiles as in (I) or out (O)
    new_graph = defaultdict(lambda: defaultdict(str))
    for i in range(num_rows):
        if (i, 0) in tiles:
            if raw[i][0] in "|F":
                counter = 1
            elif raw[i][0] != "L":
                assert False, f"Can't happen: {raw[i][0]}"
            else:
                counter = 0
            new_graph[i][0] = raw[i][0]

        else:
            counter = 0
            new_graph[i][0] = "O"

        for j in range(1, num_cols):
            if (i, j) in tiles:
                if raw[i][j] in "|F7":
                    counter = (counter + 1) % 2
                new_graph[i][j] = raw[i][j]

            else:
                total += counter
                new_graph[i][j] = "I" if counter else "O"

    print(f"Part 2: {total}")
