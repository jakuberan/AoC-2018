
def part1(data_path="input", alphabet="abcdefghijklmnopqrstuvwxyz") -> int:
    """"
    Returns checksum - multiplication of double and triple letters
    """
    occurrences23 = [0, 0]
    f = open(data_path, "r")
    for x in f:
        find23 = [True, True]

        # Check single ID
        for char in alphabet:
            if find23[0]:
                if x.count(char) == 2:
                    find23[0] = False
            if find23[1]:
                if x.count(char) == 3:
                    find23[1] = False

        # Record occurrences
        occurrences23[0] += not find23[0]
        occurrences23[1] += not find23[1]

    return occurrences23[0] * occurrences23[1]


def diff_cnt(id1: str, id2: str) -> int:
    """"
    Returns number of different characters
    """
    return sum(id1[i] != id2[i] for i in range(len(id1)))


def diff(id1: str, id2: str) -> str:
    """"
    Returns characters in common
    """
    out = ''
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            out += id1[i]

    return out


def part2(data_path="input") -> str:
    """"
    Finds a pair of IDs with single difference and returns the chars in common
    """
    f = open(data_path, "r")
    ids = []
    for x in f:
        ids.append(x)

    for i in range(len(ids)):
        for j in range(i, len(ids)):
            if diff_cnt(ids[i], ids[j]) == 1:
                return diff(ids[i], ids[j])


if __name__ == "__main__":

    print(f"Checksum is {part1()}")
    print(f"Chars in common are {part2()}")
