import numpy as np


def claim_coords(claim: str) -> list:
    """"
    Extract coordinates from claim
    """
    offset = [int(a) for a in (claim.split()[2])[:-1].split(',')]
    size = [int(a) for a in (claim.split()[3]).split('x')]

    return [offset[0], offset[0] + size[0], offset[1], offset[1] + size[1]]


def claim_size(claim: str) -> int:
    """"
    Get claim size
    """
    return int(np.prod([int(a) for a in (claim.split()[3]).split('x')]))


def claim_number(claim: str) -> int:
    """"
    Get claim number
    """
    return int(claim.split()[0][1:])


def solution(data_path="input"):
    """"
    Calculates number of overlaps and
    Returns ID of claim which does not overlap with any other
    """
    square = np.zeros([1000, 1000])

    f = open(data_path, "r")
    for x in f:
        crd = claim_coords(x)
        square[crd[0]:crd[1], crd[2]:crd[3]] += 1

    f = open(data_path, "r")
    for x in f:
        crd = claim_coords(x)
        if sum(sum(square[crd[0]:crd[1], crd[2]:crd[3]])) == claim_size(x):
            return sum(sum(square > 1)), claim_number(x)


if __name__ == "__main__":

    part_1, part_2 = solution()

    print(f"Number of overlapping fields {part_1}")
    print(f"ID of claim which does not overlap with any other: {part_2}")
