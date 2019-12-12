from day09 import intcode
from toolz import take
from typing import List

Program = List[int]
Point = List[int]


def get_step(program: Program, inp: list) -> Point:
    return list(take(2, intcode(program, inp)))



if __name__ == "__main__":

    with open("input/day11.txt") as f:
        program = [int(x) for x in f.read().strip().split(",")]


