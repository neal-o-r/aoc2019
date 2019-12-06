from typing import Tuple

Modes = Tuple[int, int, int]


def parse_opcode(opcode: int) -> Tuple[int, Modes]:
    op = opcode % 100
    modes = tuple(opcode // (100 * 10 ** i) % 10 for i in (0, 1, 2))
    return op, modes


def parse_modes(i: int, modes: Modes, ops: list) -> list:
    p1 = i + 1 if modes[0] else ops[i + 1]
    p2 = i + 2 if modes[1] else ops[i + 2]
    p3 = ops[i + 3]
    return p1, p2, p3


def update(i: int, opcode: int, modes: Modes, ops: list, input_value: int) -> list:

    p1, p2, p3 = parse_modes(i, modes, ops)

    if opcode is 1:
        val = ops[p1] + ops[p2]
        ind = p3
        step = i + 4

    elif opcode is 2:
        val = ops[p1] * ops[p2]
        ind = p3
        step = i + 4

    elif opcode is 3:
        val = input_value
        ind = p1
        step = i + 2

    elif opcode is 4:
        print(ops[p1])
        step = i + 2
        val = None
        ind = None

    elif opcode is 5:
        if ops[p1] is 0:
            step = i + 3
        else:
            step = ops[p2]
        val = None
        ind = None

    elif opcode is 6:
        if ops[p1] != 0:
            step = i + 3
        else:
            step = ops[p2]
        val = None
        ind = None

    elif opcode is 7:
        if ops[p1] < ops[p2]:
            val = 1
            ind = p3
        else:
            val = 0
            ind = p3
        step = i + 4

    elif opcode is 8:
        if ops[p1] == ops[p2]:
            val = 1
            ind = p3
        else:
            val = 0
            ind = p3
        step = i + 4

    return step, [o if i != ind else val for i, o in enumerate(ops)]


def run_intcode(i, ops, input_value=1):
    opcode, modes = parse_opcode(ops[i])

    if opcode == 99:
        return ops
    i, ops = update(i, opcode, modes, ops, input_value)
    return run_intcode(i, ops, input_value)


if __name__ == "__main__":

    with open("input/day05.txt", "r") as f:
        program = [int(x) for x in f.read().split(",")]

    run_intcode(0, program, 1)

    with open("input/day05.txt", "r") as f:
        program = [int(x) for x in f.read().split(",")]

    run_intcode(0, program, 5)
