import string
from collections import Counter

MAP = {k: v for k, v in zip("23456789TJQKA", string.ascii_lowercase)}
PART_2_MAP = {k: v for k, v in zip("J23456789TQKA", string.ascii_lowercase)}


def _primary_rank(hand: str) -> int:
    vals = Counter(hand)
    cvals = Counter(vals.values())
    if len(vals) == 5:
        # High card
        return 0
    elif len(vals) == 4:
        # Pair
        return 1
    elif cvals.get(2, 0) == 2:
        # Two pair
        return 2
    elif cvals.get(3, 0) == 1:
        if cvals.get(2, 0) == 1:
            # Full house
            return 4
        else:
            # Three of a kind
            return 3
    elif cvals.get(4, 0) == 1:
        # Four of a kind
        return 5
    else:
        # Five of a kind
        return 6


class Hand:
    def __init__(self, hand: str, primary_rank: int | None = None):
        self.hand = hand
        assert len(hand) == 5

        the_map = PART_2_MAP if primary_rank is not None else MAP
        self.ordered_hand = "".join(the_map[k] for k in hand)

        self.primary_rank = primary_rank or _primary_rank(hand)

    @classmethod
    def for_part2(cls, hand: str) -> "Hand":
        # Maximizes value if all Js get set to same value
        vals = {h for h in hand if h != "J"}
        vals = vals or {"A"}  # Deal with the case of 5 Js
        my_primary_rank = max(_primary_rank(hand.replace("J", v)) for v in vals)
        hand = Hand(hand, primary_rank=my_primary_rank)
        return hand

    def __eq__(self, other: "Hand") -> bool:
        return self.hand == other.hand

    def __hash__(self) -> int:
        return hash(self.ordered_hand)

    def __le__(self, other: "Hand") -> bool:
        return (self.primary_rank, self.ordered_hand) <= (
            other.primary_rank,
            other.ordered_hand,
        )

    def __lt__(self, other: "Hand") -> bool:
        return (self <= other) and (self != other)

    def __repr__(self) -> str:
        return f"<Hand({self.hand=}, {self.ordered_hand=}, {self.primary_rank=})>"


def _parse_file(input_file: str, is_part_2: bool = False) -> list[tuple[Hand, int]]:
    out = []
    with open(input_file, "rt") as inf:
        for line in inf:
            hand, bid = line.split(" ")
            bid = int(bid)
            out.append((Hand.for_part2(hand) if is_part_2 else Hand(hand), bid))
    return out


def part1(input_file: str):
    data = _parse_file(input_file)
    out = list(sorted(data))
    print(f"Part 1: {sum(i * o[1] for i, o in enumerate(out, 1))}")


def part2(input_file: str):
    data = _parse_file(input_file, is_part_2=True)
    out = list(sorted(data))
    print(f"Part 2: {sum(i * o[1] for i, o in enumerate(out, 1))}")
