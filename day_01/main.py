import numpy as np

if __name__ == "__main__":

    # Define parameters
    data_path = "input"
    freq = 0

    # Read and process for the first part
    f = open(data_path, "r")
    for x in f:
        freq += int(x)

    print(f"Final frequency is {freq}")

    # Params for part 2
    reached = {0}
    keep_searching = True
    freq = 0

    # Read and process for the second part
    while keep_searching:
        f = open(data_path, "r")
        for x in f:
            freq += int(x)
            if freq in reached:
                keep_searching = False
                break
            else:
                reached.add(freq)

    print(f"First frequency reached twice is {freq}")
