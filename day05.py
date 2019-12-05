from typing import Tuple, List

Modes = Tuple[int, int, int]
Ops = List[int]

op_code_params = {1 : 3, 2 : 3, 3 : 1, 4 : 1}


def string_to_ints(text : str, delimiter : str = ',') -> list:
    return [int(i) for i in text.split(delimiter)]


def parse_opcode(opcode : int) -> Tuple[int, Modes, int]:
    op = opcode % 100
    modes = tuple(opcode // (100 * 10**i) % 10 for i in (0, 1, 2))
    nparams = op_code_params[op]
    return op, modes, nparams


def get_params(i : int , ops : Ops) -> list:
    op = ops[i]
    if op is 1 or op is 2:
        return ops[i + 1 : i + op_code_params[op] + 1]
    elif op is 3 or op is 4:
        return [ops[i + 1]]


def parse_modes(params : list, modes : Modes, ops : Ops) -> list:
    pout = []
    for p, m in zip(params, modes):
        if m is 0:
            pout.append(ops[p])
        elif p is 1:
            pout.append(p)
    return pout


def update(i : int, ops : Ops, input_val : int) -> Ops:
    op, modes, _ = parse_opcode(ops[i])
    if op is 1:
        params = parse_modes(get_params(i, ops), modes, ops)
        print(params)
        val = params[0] + params[1]
        ind = params[2]
    elif op is 2:
        params = parse_modes(get_params(i, ops), modes, ops)
        val = params[0] * params[1]
        ind = params[2]
    elif op is 3:
        val = input_val
        ind = get_params(i, ops)[0]
    elif op is 4:
        print(get_params(i, ops)[0])

    print(val, ind)
    return [v if i != ind else val for i, v in enumerate(ops)]


def run(i : int, ops : Ops, input_val : int = 1) -> Ops:
    op, _, nparams = parse_opcode(ops[i])
    if op is 99:
        return ops
    return run(i + nparams + 1, update(i, ops, input_val))


if __name__ == "__main__":
    with open("input/day05.txt") as f:
        text = f.read().strip()

    ops = string_to_ints(text)
