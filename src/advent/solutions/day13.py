import numpy as np


def _parse_file(input_file: str) -> list[np.ndarray]:
    out = []
    with open(input_file, "rt") as inf:
        cur = []
        for line in inf:
            line = line.strip()
            if not line:
                out.append(np.array(cur))
                cur = []
            else:
                cur.append([x for x in line])
        out.append(np.array(cur))

    return out


def part1(input_file: str):
    data = _parse_file(input_file)
    total = 0
    for datum in data:
        for i in range(1, datum.shape[0]):
            if i + i > datum.shape[0]:
                l = datum.shape[0] - i
            else:
                l = i
            if (datum[i - l : i, :] == datum[i : i + l, :][::-1, :]).all():
                total += 100 * i
                break

        for i in range(1, datum.shape[1]):
            if i + i > datum.shape[1]:
                l = datum.shape[1] - i
            else:
                l = i
            if (datum[:, i - l : i] == datum[:, i : i + l][:, ::-1]).all():
                total += i
                break
    print(f"Part 1: {total}")


def part2(input_file: str):
    data = _parse_file(input_file)
    total = 0
    for datum in data:
        for i in range(1, datum.shape[0]):
            if i + i > datum.shape[0]:
                l = datum.shape[0] - i
            else:
                l = i
            if (datum[i - l : i, :] != datum[i : i + l, :][::-1, :]).sum() == 1:
                total += 100 * i
                break

        for i in range(1, datum.shape[1]):
            if i + i > datum.shape[1]:
                l = datum.shape[1] - i
            else:
                l = i
            if (datum[:, i - l : i] != datum[:, i : i + l][:, ::-1]).sum() == 1:
                total += i
                break
    print(f"Part 2: {total}")
