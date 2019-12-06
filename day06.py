from collections import defaultdict
from typing import Dict

Orbits = Dict[str, set]


def direct_orbits(pairs: list, reverse : bool = False) -> Orbits:
    d = defaultdict(set)
    for p in pairs:
        k, v = p.split(")") if not reverse else p.split(")")[::-1]
        d[k].add(v)
    return d


def recursive_search(obj: str, orbits: Orbits, lst: list = []) -> set:
    if obj not in orbits:
        return lst
    return sum((recursive_search(o, orbits, lst + [o]) for o in orbits[obj]), [])


if __name__ == "__main__":

    with open("input/day06.txt") as f:
        text = f.read().strip().split("\n")

    orbit = direct_orbits(text)

    n_orb = sum(len(set(recursive_search(o, orbit))) for o in orbit)
    print(n_orb)

    reverse_orbits = direct_orbits(text, reverse=True)
    n_trans = len(set(recursive_search("YOU", reverse_orbits)) ^
                  set(recursive_search("SAN", reverse_orbits)))
    print(n_trans)
