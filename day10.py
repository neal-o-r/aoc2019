from itertools import cycle
from typing import List, Tuple
from math import atan2, sqrt, pi, hypot
from collections import defaultdict


Point = Tuple[int, int]
Points = List[Point]


def get_pts(txt: str) -> Points:
    n = sqrt(len(txt))
    return [(int(i % n), int(i // n)) for i, x in enumerate(txt) if x is '#']


def angle(a: Point, b: Point) -> float:
    a = atan2(b[0] - a[0], b[1] - a[1])
    return round((2*pi - a) % (2 * pi), 5)


def count_angles(pt: Point, pts: Points) -> int:
    return len(set(angle(p, pt) for p in pts if pt != p))


def dist(a: Point, b: Point) -> float:
    return hypot((a[0] - b[0]), (b[1] - a[1]))


def part2(pts: Points, n: int) -> Point:
    loc = max(pts, key=lambda x: count_angles(x, pts))
    pts = [p for p in pts if p != loc]
    # order pts by distance to loc
    d = defaultdict(list)
    for p in pts:
        a = angle(p, loc)
        d[a] += [p]

    d = {a: sorted(l, key=lambda x: dist(loc, x)) for a, l in d.items()}
    i = 0
    for a in cycle(sorted(set(angle(p, loc) for p in pts))):
        if d[a] != []:
            pt = d[a].pop(0)
            i += 1
            if i == n:
                return pt


if __name__ == "__main__":

    with open("input/day10.txt") as f:
        txt = f.read().replace("\n", "")

    pts = get_pts(txt)
    print(max(count_angles(p, pts) for p in pts))
