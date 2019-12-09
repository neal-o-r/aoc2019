import numpy as np

def split(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]


def count(l, v):
    return sum(map(lambda x: 1 if x == v else 0, l))


def collapse(layers):
    return [next(filter(lambda v: v != 2, lay)) for lay in zip(*layers)]


def draw(img):
    for r in img:
        print(*['#' if x == 1 else ' ' for x in r])


if __name__ == "__main__":

    lenx, leny = 25, 6
    data = [int(x) for x in open('input/day08.txt').read().strip('\n')]

    layers = split(data, lenx*leny)
    best = min(layers, key=lambda l: count(l, 0))
    print(count(best, 1) * count(best, 2))

    img = split(collapse(layers), lenx)
    draw(img)

