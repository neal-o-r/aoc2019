from day09 import intcode
from toolz import take
from typing import List, Generator
from collections import defaultdict

N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
L = {N: W, E: N, S: E, W: S}
R = {N: E, E: S, S: W, W: N}

def print_grid(grid):
    pts = list(zip(*grid))
    xmax, xmin = max(pts[0]) + 1, min(pts[0])
    ymax, ymin = max(pts[1]) + 1, min(pts[1])

    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            c = '#' if grid[(x, y)] else ' '
            print(c, end='')

        print()


if __name__ == "__main__":

    with open("input/day11.txt") as f:
        program = [int(x) for x in f.read().strip().split(",")]

    inp = []
    intgen = intcode(program, inp)
    grid = defaultdict(int)
    pos = (0, 0)
    facing = N

    grid[pos] = 1
    while True:
        inp.append(grid[pos])
        try:
            color = next(intgen)
            direction = next(intgen)
            grid[pos] = color
            facing = R[facing] if direction else L[facing]
            pos = (pos[0] + facing[0], pos[1] + facing[1])
        except StopIteration:
            break


