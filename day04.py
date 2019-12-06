from collections import Counter


def monotonic(n: int) -> bool:
    n_str = str(n)
    return list(n_str) == sorted(n_str)


def has_adjacent_pair(n: int) -> bool:
    n_str = str(n)
    return any(v >= 2 for v in Counter(n_str).values())


def has_adjacent_pair_only(n: int) -> bool:
    n_str = str(n)
    return any(v == 2 for v in Counter(n_str).values())


def check_num(n: int) -> bool:
    return has_adjacent_pair_only(n) and monotonic(n)


if __name__ == "__main__":

    num_pwords = sum(check_num(n) for n in range(134564, 585159))
    print(num_pwords)
