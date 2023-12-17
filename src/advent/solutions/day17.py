import heapq
import itertools as its


def _parse_file(input_file: str) -> list[list[int]]:
    with open(input_file, "rt") as inf:
        return [[int(x) for x in line.strip()] for line in inf]


TURNS = {
    ">": "^v",
    "<": "^v",
    "v": "<>",
    "^": "<>",
}

DIFF = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def part1(input_file: str):
    data = _parse_file(input_file)
    num_rows = len(data)
    num_cols = len(data[0])

    # (total loss, row, col, dir, count in dir)
    queue = [
        (data[0][1], 0, 1, ">", 1, [(0, 1, ">")]),
        (data[1][0], 1, 0, "v", 1, [(1, 0, "v")]),
    ]

    seen: set[(int, int, str, int)] = set()

    heapq.heapify(queue)
    while True:
        loss, row, col, dir, count, path = heapq.heappop(queue)
        if (row == num_rows - 1) and (col == num_cols - 1):
            # import sys
            # path = {(i, j): v for i, j, v in path}
            # for i, line in enumerate(data):
            #     for j, x in enumerate(line):
            #         sys.stdout.write(path.get((i, j), str(x)))
            #     print()
            print(f"Part 1: {loss}")
            return

        for turn, my_count in its.chain(
            zip(TURNS[dir], its.cycle([1])), [(dir, count + 1)]
        ):
            if my_count > 3:
                continue

            i, j = DIFF[turn]
            new_row, new_col = row + i, col + j
            if not ((0 <= new_col < num_cols) and (0 <= new_row < num_rows)):
                continue
            new_loss = loss + data[new_row][new_col]
            if (new_row, new_col, turn, my_count) in seen:
                continue
            seen.add((new_row, new_col, turn, my_count))
            heapq.heappush(
                queue,
                (
                    new_loss,
                    new_row,
                    new_col,
                    turn,
                    my_count,
                    path + [(new_row, new_col, turn)],
                ),
            )


def part2(input_file: str):
    data = _parse_file(input_file)
    num_rows = len(data)
    num_cols = len(data[0])

    # (total loss, row, col, dir, count in dir)
    queue = [
        (data[0][1], 0, 1, ">", 1, [(0, 1, ">")]),
        (data[1][0], 1, 0, "v", 1, [(1, 0, "v")]),
    ]

    seen: set[(int, int, str, int)] = set()

    heapq.heapify(queue)
    while True:
        loss, row, col, dir, count, path = heapq.heappop(queue)
        if (row == num_rows - 1) and (col == num_cols - 1):
            if count >= 4:
                # import sys
                # path = {(i, j): v for i, j, v in path}
                # for i, line in enumerate(data):
                #     for j, x in enumerate(line):
                #         sys.stdout.write(path.get((i, j), str(x)))
                #     print()
                print(f"Part 2: {loss}")
                return

        next_steps = []
        if count < 10:
            next_steps.append((dir, count + 1))
        if count >= 4:
            next_steps.extend(zip(TURNS[dir], its.cycle([1])))

        for turn, my_count in next_steps:
            i, j = DIFF[turn]
            new_row, new_col = row + i, col + j
            if not ((0 <= new_col < num_cols) and (0 <= new_row < num_rows)):
                continue
            new_loss = loss + data[new_row][new_col]
            if (new_row, new_col, turn, my_count) in seen:
                continue
            seen.add((new_row, new_col, turn, my_count))
            heapq.heappush(
                queue,
                (
                    new_loss,
                    new_row,
                    new_col,
                    turn,
                    my_count,
                    path + [(new_row, new_col, turn)],
                ),
            )
