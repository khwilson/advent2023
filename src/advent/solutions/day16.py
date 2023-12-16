from tqdm.cli import tqdm


def _parse_file(input_file: str) -> list[str]:
    with open(input_file, "rt") as inf:
        return [line.strip() for line in inf]


DIR_CHANGE = {
    ".": {
        ">": [(0, 1, ">")],
        "^": [(-1, 0, "^")],
        "<": [(0, -1, "<")],
        "v": [(1, 0, "v")],
    },
    "/": {
        ">": [(-1, 0, "^")],
        "^": [(0, 1, ">")],
        "<": [(1, 0, "v")],
        "v": [(0, -1, "<")],
    },
    "\\": {
        "<": [(-1, 0, "^")],
        "v": [(0, 1, ">")],
        ">": [(1, 0, "v")],
        "^": [(0, -1, "<")],
    },
    "|": {
        ">": [(-1, 0, "^"), (1, 0, "v")],
        "^": [(-1, 0, "^")],
        "<": [(-1, 0, "^"), (1, 0, "v")],
        "v": [(1, 0, "v")],
    },
    "-": {
        ">": [(0, 1, ">")],
        "^": [(0, 1, ">"), (0, -1, "<")],
        "<": [(0, -1, "<")],
        "v": [(0, -1, "<"), (0, 1, ">")],
    },
}

for v in DIR_CHANGE.values():
    for vv in v.values():
        for vvv in vv:
            assert vvv in [(-1, 0, "^"), (1, 0, "v"), (0, 1, ">"), (0, -1, "<")]


def _run(data: list[str], start_i: int, start_j: int, start_d: str) -> int:
    queue: list[(int, int, str)] = [(start_i, start_j, start_d)]

    lights: list[list[set[str]]] = [[set() for _ in range(len(line))] for line in data]

    lights[start_i][start_j] |= {start_d}

    num_cols = len(data[0])
    num_rows = len(data)
    while queue:
        i, j, d = queue[0]
        queue = queue[1:]

        mirror = data[i][j]
        for di, dj, dd in DIR_CHANGE[mirror][d]:
            qi, qj = i + di, j + dj
            if 0 <= qi < num_rows:
                if 0 <= qj < num_cols:
                    if dd not in lights[qi][qj]:
                        lights[qi][qj] |= {dd}
                        queue.append((qi, qj, dd))
    total = sum(bool(y) for x in lights for y in x)
    return total


def part1(input_file: str):
    data = _parse_file(input_file)
    total = _run(data, 0, 0, ">")
    print(f"Part 1: {total}")


def part2(input_file: str):
    data = _parse_file(input_file)
    num_rows = len(data)
    num_cols = len(data[0])
    total = 0
    with tqdm(total=2 * num_cols + 2 * num_rows) as pbar:
        for i in range(num_rows):
            total = max(total, _run(data, i, 0, ">"))
            pbar.update(1)
        for j in range(num_cols):
            total = max(total, _run(data, 0, j, "v"))
            pbar.update(1)
        for i in range(num_rows):
            total = max(total, _run(data, i, num_cols - 1, "<"))
            pbar.update(1)
        for j in range(num_cols):
            total = max(total, _run(data, num_rows - 1, 0, "^"))
            pbar.update(1)

    print(f"Part 2: {total}")
