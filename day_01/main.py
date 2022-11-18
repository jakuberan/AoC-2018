import numpy as np

def part1(data_path = "input"):
    freq = 0
    f = open(data_path, "r")
    for x in f:
        freq += int(x)
    return freq

def part2(data_path = "input"):
    reached = {0}
    freq = 0

    # Read and process for the second part
    while True:
        f = open(data_path, "r")
        for x in f:
            freq += int(x)
            if freq in reached:
                return freq
            else:
                reached.add(freq)


if __name__ == "__main__":

    print(f"Final frequency is {part1()}")
    print(f"First frequency reached twice is {part2()}")
