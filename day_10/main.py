import numpy as np


def read_and_process(data_path: str):
    """
    Returns an array of coordinates and velocities
    """

    f = open(data_path, "r")
    out = []
    for x in f:
        sep = [c for c in x.strip().replace(',', ' ').replace('<', ' ').replace('>', ' ').split()]
        out.append([int(sep[1]), int(sep[2]), int(sep[4]), int(sep[5])])
    return np.array(out)


def calc_next_distance(points) -> int:
    """
    Calculate auxiliary distance by difference between max and min coordinates
    of the next point 
    """
    x_new = points[:, 0] + points[:, 2]
    y_new = points[:, 1] + points[:, 3]
    
    x_dist = max(x_new) - min(x_new)
    y_dist = max(y_new) - min(y_new)
    
    return x_dist + y_dist
    

def print_plane(points) -> None:
    """
    Prints out final plane with points
    """
    
    # Adjust filed
    points[:, 0] -= min(points[:, 0])
    points[:, 1] -= min(points[:, 1])
    
    # Initialize empty plane
    out = []
    for i in range((max(points[:, 1]) + 1)):
        out.append(['.'] * (max(points[:, 0]) + 1))
    
    # Add stars
    for i in range(points.shape[0]):
        out[points[i, 1]][points[i, 0]] = '#'
    
    # Print plane
    for r in range(len(out)):
        print(''.join(out[r]))
    

def part_1(data_path="input"):
    """
    Identify the message and calculate the seconds
    """
    points = read_and_process(data_path)
    distance = np.inf
    seconds = 0

    # Iterate plane
    while calc_next_distance(points) <= distance:
        seconds += 1
        distance = calc_next_distance(points)
        points[:, 0] += points[:, 2]
        points[:, 1] += points[:, 3]
        
    print_plane(points)
    return seconds


if __name__ == "__main__":

    print(f"One needs to waits {part_1()} seconds before the message appears")
