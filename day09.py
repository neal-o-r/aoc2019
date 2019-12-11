from collections import defaultdict
from typing import List, Generator, Tuple, Dict

Program = List[int]
Input = List[int]
Output = Generator[int, int, int]
Modes = List[int]


nargs = {0: 0, 1: 4, 2: 4, 3: 2, 4: 2,
         5: 3, 6: 3, 7: 4, 8: 4, 9: 2}


def parse_opcode(opcode: int) -> Tuple[int, Modes]:
    op = opcode % 100
    modes = [(opcode // 10 ** i) % 10 for i in range(2, 5)]
    return op, modes


def intcode(program: Program, program_input: Input) -> Output:

    i, offset = 0, 0
    memory = defaultdict(int, enumerate(program))
    while True:
        op, modes = parse_opcode(memory[i])
        if op is 99:
            return
        size = nargs[op]
        args = [memory[i + x] for x in range(1, size)]

        reads = [(memory[x], x, memory[x + offset])[m]
                    for x, m in zip(args, modes)]
        write = [(x, None, x + offset)[m] for x, m in zip(args, modes)]
        i += size
        if op is 1:
            memory[write[2]] = reads[0] + reads[1]
        elif op is 2:
            memory[write[2]] = reads[0] * reads[1]
        elif op is 3:
            memory[write[0]] = program_input.pop(-1)
        elif op is 4:
            yield reads[0]
        elif op is 5 and reads[0]:
            i = reads[1]
        elif op is 6 and not reads[0]:
            i = reads[1]
        elif op is 7:
            memory[write[2]] = int(reads[0] < reads[1])
        elif op is 8:
            memory[write[2]] = int(reads[0] == reads[1])
        elif op is 9:
            offset += reads[0]


if __name__ == "__main__":

    with open("input/day09.txt") as f:
        program = [int(x) for x in f.read().split(",")]

    print(list(intcode(program, [1])))
    print(list(intcode(program, [2])))
