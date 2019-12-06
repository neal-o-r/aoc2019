from collections import defaultdict
from typing import Dict

Orbits = Dict[str, set]


def direct_orbits(pairs: list) -> Orbits:
    d = defaultdict(set)
    for p in pairs:
        k, v = p.split(")")
        d[k].add(v)
    return d


def recursive_search(obj: str, orbits: Orbits, lst: list = []) -> set:
    if obj not in orbits:
        return lst
    return sum((recursive_search(o, orbits, lst + [o]) for o in orbits[obj]), [])


def transfers(obj: str, orbits: Orbits, visited: set = set(), val: int = 0) -> int:
    if "SAN" in orbits[obj]:
        return val - 1
    to_check = orbits[obj] - visited
    return sum(transfers(o, orbits, visited | set([o]), val + 1) for o in to_check)


def invert_orbits(orbits: Orbits) -> Orbits:
    keys = list(orbits.keys())
    vals = list(orbits.values())

    for k, v in zip(keys, vals):
        for vi in v:
            orbits[vi].add(k)

    return orbits


if __name__ == "__main__":

    with open("input/day06.txt") as f:
        text = f.read().strip().split("\n")

    orbit = direct_orbits(text)

    n_orb = sum(len(set(recursive_search(o, orbit))) for o in orbit)
    print(n_orb)

    all_connections = invert_orbits(orbit)
    n_trans = transfers("YOU", all_connections)
    print(n_trans)
