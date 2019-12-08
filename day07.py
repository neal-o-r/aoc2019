from day05 import update, parse_opcode
from typing import Iterator
from itertools import permutations


def run_intcode(i: int, ops: list, input_iter: Iterator, output: list = []) -> list:
    opcode, modes = parse_opcode(ops[i])

    if opcode == 99:
        return ops, output
    i, ops, output = update(i, opcode, modes, ops, input_iter)
    return run_intcode(i, ops, input_iter, output)


def run_sequence(settings : list, ops: list) -> int:
    output = [0]
    for s in settings:
        _, o = run_intcode(0, ops, iter([s, output[-1]]))
        output += o

    return output


if __name__ == "__main__":

    with open("input/day07.txt") as f:
        program = [int(x) for x in f.read().split(",")]

    program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    settings = list(range(5, 10))

    # perms = list(permutations(settings))
    # thrusts = [run_sequence(sp, program)[-1] for sp in perms]
    # print("Max: ", max(thrusts))

