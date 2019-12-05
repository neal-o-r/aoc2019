from operator import add, mul


def string_to_ints(text : str, delimiter : str = ',') -> list:
    return [int(i) for i in text.split(delimiter)]


def update(i : int, all_ops : list) -> list:

    op_type, left_index, right_index, to_index = all_ops[i:i+4]
    f = add if op_type is 1 else mul

    val = f(all_ops[left_index], all_ops[right_index])

    return [a if i != to_index else val for i, a in enumerate(all_ops)]


def run(i : int, all_ops: list) -> list:

    if all_ops[i] is 99:
        return all_ops
    return run(i+4, update(i, all_ops))


def check_inputs(inputs : tuple, ops : list, value : int) -> bool:
    ops[1], ops[2] = inputs
    return run(0, ops)[0] == value


if __name__ == "__main__":
    with open("input/day02.txt") as f:
        ops = string_to_ints(f.read())

    # do pre-flight changes
    ops[1] = 12
    ops[2] = 2

    final_state = run(0, ops)
    print(final_state[0])

    for i in range(0, 100):
        for j in range(0, 100):
            if check_inputs((i, j), ops, 19690720):
                print(100 * i + j)
