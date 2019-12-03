from typing import List, Tuple, Dict

# Define types
Point = Tuple[int, int]
Points = List[Point]
PointPath = Dict[Point, int]
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


def points_from_path(loc: Point, path: Path) -> PointPath:
    """
    Turn a path into a list of points traversed on the path
    return this as a dict, mapping point to when it was passed through
    """
    points = [loc]
    for step in path:
        segment = take_step(loc, step)
        points.extend(segment)
        loc = segment[-1]

    return {p: i for i, p in enumerate(points)}


def intersections(points1: PointPath, points2: PointPath) -> Points:
    p1_list = list(points1.keys())[1:]
    p2_list = list(points2.keys())[1:]
    return list(set(p1_list) & set(p2_list))


def manhattan_distance_to_origin(pt: Point) -> int:
    return abs(pt[0]) + abs(pt[1])


def total_steps_to_pt(
    intersection: Point, points1: PointPath, points2: PointPath
) -> int:
    return points1[intersection] + points2[intersection]


if __name__ == "__main__":

    with open("input/day03.txt") as f:
        lines = f.read().strip().split("\n")

    paths = [parse_input(l) for l in lines]
    points = [points_from_path((0, 0), path) for path in paths]

    inters = intersections(*points)

    min_pt = min(inters, key=manhattan_distance_to_origin)
    print(min_pt, manhattan_distance_to_origin(min_pt))

    total_steps = lambda x: total_steps_to_pt(x, *points)
    min_steps = min(inters, key=total_steps)
    print(min_steps, total_steps(min_steps))
