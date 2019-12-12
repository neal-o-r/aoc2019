from typing import List, Tuple
from operator import add
from collections import namedtuple
import re

class Point(namedtuple('Point', ['x', 'y', 'z', 'vx', 'vy', 'vz'])):
    pass


Position = Tuple[int, int, int]
Velocity = Tuple[int, int, int]
Points = List[Point]


def parse_input(txt: list) -> Points:
    parse_position = lambda x: tuple(map(int, re.findall('[-]?\d+', x)))

    return [Point(*p, 0,0,0) for p in map(parse_position, txt)]


def update_velocity(p: Point, pos: Points) -> Velocity:
    update = lambda a, b: (a < b) - (a > b)
    vx, vy, vz = p.vx, p.vy, p.vz
    for pi in pos:
        vx += update(p.x, pi.x)
        vy += update(p.y, pi.y)
        vz += update(p.z, pi.z)

    return Point(p.x, p.y, p.z, vx, vy, vz)



def take_step(pos: Points) -> Points:

    new_vel = update_velocity()

    update = lambda a, b: t

    return list(update(p, v) for p, v in zip(pos, vels))


def energy(pos):
    pot = (sum(map(abs, p)) for p in pos)
    kin = (sum(abs(v) for v in velocity(p, pos)) for p in pos)

    return sum(pot) + sum(kin)


if __name__ == "__main__":

    pos = parse_input("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".split("\n"))

    # for _ in range(10):
        # pos = take_step(pos)
        # print(energy(pos))
