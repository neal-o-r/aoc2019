from typing import List, Tuple, Dict

# Define types
Point = Tuple[int, int]
Points = List[Point]
Step = Tuple[str, int]
Path = List[Step]


def parse_input(text: str) -> Path:
    steps = text.split(",")
    return [(s[0], int(s[1:])) for s in steps]


def take_step(loc: Point, step: Step) -> Points:
    """
    create a list of points traversed in
    taking a step, in some direction
    """
    direction, length = step
    if direction is "U":
        return [(loc[0], loc[1] + i) for i in range(1, length + 1)]
    elif direction is "D":
        return [(loc[0], loc[1] - i) for i in range(1, length + 1)]
    elif direction is "R":
        return [(loc[0] + i, loc[1]) for i in range(1, length + 1)]
    else:
        return [(loc[0] - i, loc[1]) for i in range(1, length + 1)]


def points_from_path(loc: Point, path: Path) -> Points:
    """
    Turn a path into a list of points traversed on the path
    """
    points = [loc]
    for step in path:
        segment = take_step(loc, step)
        points.extend(segment)
        loc = segment[-1]

    return points


def intersections(points1: Points, points2: Points) -> Points:
    return list(set(points1[1:]) & set(points2[1:]))


def manhattan_distance_to_origin(pt: Point) -> int:
    return abs(pt[0]) + abs(pt[1])


def steps_taken(pt: Point, points1: Points, points2: Points) -> int:
    return points1.index(pt) + points2.index(pt)


if __name__ == "__main__":

    with open("day03.txt") as f:
        lines = f.read().strip().split("\n")

    paths = [parse_input(l) for l in lines]
    points = [points_from_path((0, 0), path) for path in paths]

    inters = intersections(*points)

    min_pt = min(inters, key=manhattan_distance_to_origin)
    print(min_pt, manhattan_distance_to_origin(min_pt))

    steps = lambda x: steps_taken(x, *points)
    min_steps = min(inters, key=steps)
    print(min_steps, steps_taken(min_steps, *points))
