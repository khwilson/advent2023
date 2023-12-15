def _parse_file(input_file: str) -> list[str]:
    with open(input_file, "rt") as inf:
        return next(inf).strip().split(",")


def _hash(val: str) -> int:
    h = 0
    for x in val:
        h = ((h + ord(x)) * 17) % 256
    return h


def part1(input_file: str):
    data = _parse_file(input_file)
    total = sum(map(_hash, data))
    print(f"Part 1: {total}")


def part2(input_file: str):
    data = _parse_file(input_file)
    boxes = [[] for _ in range(256)]
    for val in data:
        if val[-1] == "-":
            label = val[:-1]
            op = "-"
            num = None
        else:
            label = val[:-2]
            op = "="
            num = int(val[-1])

        box_num = _hash(label)
        box = boxes[box_num]
        ls = [i for i, l in enumerate(box) if l[0] == label]

        if op == "=":
            if ls:
                idx = ls[0]
                box = box[:idx] + [(label, num)] + box[idx + 1 :]
            else:
                box.append((label, num))
        elif ls:
            idx = ls[0]
            box = box[:idx] + box[idx + 1 :]

        boxes[box_num] = box

    total = 0
    for box_num, box in enumerate(boxes, 1):
        total += sum(box_num * idx * x[1] for idx, x in enumerate(box, 1))

    print(f"Part 2: {total}")
