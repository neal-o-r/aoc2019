from day05 import update, parse_opcode
from typing import Iterator
from itertools import permutations


def run_intcode(i: int, ops: list, input_iter: Iterator, output: list = []) -> list:
    opcode, modes = parse_opcode(ops[i])

    if opcode == 99:
        return i, ops, output

    i, ops, output = update(i, opcode, modes, ops, input_iter)
    return run_intcode(i, ops, input_iter, output)


def run_intcode_halt(i: int, ops: list, input_iter: Iterator, output: list = []) -> list:
    opcode, modes = parse_opcode(ops[i])

    if opcode == 99:
        return i, ops, output, True
    if opcode == 4:
        i, ops, output = update(i, opcode, modes, ops, input_iter)
        return i, ops, output, False

    i, ops, output = update(i, opcode, modes, ops, input_iter)
    return run_intcode_halt(i, ops, input_iter, output)


def run_sequence(settings : list, ops: list) -> list:
    output = [0]
    for s in settings:
        _, _ , o = run_intcode(0, ops, iter([s, output[-1]]))
        output += o

    return output


def run_feedback(settings : list, ops: list) -> list:
    output = [0]
    op_out = []
    i_out = []
    for s in settings:
        i, op, o = run_intcode(0, ops, iter([s, output[-1]]))
        output += o
        op_out.append(op)
        i_out.append(i)

    c = 0
    halts = [False] * len(settings)
    inputs = [[o_i, s_i] for o_i, s_i in zip(output, settings)]

    while not halts[-1]:

        i, op, o, halt = run_intcode_halt(i_out[c], op_out[c], iter(inputs[c]))
        halts[c % 5] = halt
        output += o
        op_out[c % 5] = op
        c = (c + 1) % 5

    return output


if __name__ == "__main__":

    with open("input/day07.txt") as f:
        program = [int(x) for x in f.read().split(",")]

    settings = list(range(0, 5))
    program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    settings = [9,8,7,6,5]
    # perms = list(permutations(settings))
    # thrusts = [run_sequence(sp, program)[-1] for sp in perms]
    # print("Max: ", max(thrusts))

