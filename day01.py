def fuel_required_for_mass(mass: int) -> int:
    return (mass // 3) - 2


def recursive_fuel_required(mass: int) -> int:
    """
    takes a mass, and computes the fuel requires, and the fuel
    that requires etc etc.
    """
    fuel = fuel_required_for_mass(mass)
    if fuel <= 0:
        return 0
    return fuel + recursive_fuel_required(fuel)


if __name__ == "__main__":
    with open("input/day01.txt") as f:
        lines = f.read().strip().split("\n")

    total_fuel = sum(fuel_required_for_mass(int(m)) for m in lines)
    print(total_fuel)

    recursive_total_fuel = sum(recursive_fuel_required(int(m)) for m in lines)
    print(recursive_total_fuel)
