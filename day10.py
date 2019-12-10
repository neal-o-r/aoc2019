from itertools import cycle
from typing import List, Tuple
from math import atan2, sqrt, pi
from collections import defaultdict


Point = Tuple[int, int]
Points = List[Point]


def get_pts(txt: str) -> Points:
    n = sqrt(len(txt))
    return [(int(i % n), int(i // n)) for i, x in enumerate(txt) if x is '#']


def angle(a: Point, b: Point) -> float:
    a = atan2(b[1] - a[1], b[0] - a[0])
    return round(a if a >= 0 else abs(a) + pi, 5)


def all_angles(pt, pts: Points) -> int:
    return [angle(pt, p) if p != pt else None for p in pts]


def compute_all_angles(pts: Points) -> list:
    return [all_angles(p, pts) for p in pts]


def dist(a: Point, b: Point) -> float:
    return sqrt((a[0] - a[1])**2 + (b[0] - b[1])**2)


def all_dists(pt: Point, pts: Points) -> list:
    return [dist(pt, p) if p != pt else None for p in pts]




if __name__ == "__main__":

    with open("input/day10.txt") as f:
        txt = f.read().replace("\n", "")

    pts = get_pts(txt)
    all_ang = compute_all_angles(pts)

    count = lambda x: len(set(x)) - 1
    views = list(map(count, all_ang))


    print(max(views))
