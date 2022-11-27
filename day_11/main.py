import numpy as np
from scipy.signal import convolve2d


def solution(serial_number: int, size=300):
    """
    Calculate biggest power grid coordinates
    """
    # Initialize x and y coordinate arrays
    cells_x = np.ones([size, size])
    cells_y = np.ones([size, size])
    
    for i in range(300):
        cells_x[i, :] = range(11, size+11)
        cells_y[:, i] = range(1, size+1)
        
    # Apply operations to calcul
    cells = np.multiply(np.multiply(cells_x, cells_y) + serial_number, cells_x)
    cells = np.floor(cells / 100) % 10 - 5
    
    # Convolution to calculate 3x3 sum and find maximum
    ones = np.ones([3, 3])
    conv = convolve2d(cells, ones, mode='valid')
    idx = np.unravel_index(np.argmax(conv, axis=None), conv.shape)
    
    # Use any convolution
    max_so_far = 0
    dim_best = None
    idx2 = None
    for dim in range(1, 30):
        ones = np.ones([dim, dim])
        conv = convolve2d(cells, ones, mode='valid')
        if np.max(conv) > max_so_far:
            max_so_far = np.max(conv)
            idx2 = np.unravel_index(np.argmax(conv, axis=None), conv.shape)
            dim_best = dim
    
    return f"{idx[1]+1},{idx[0]+1}", f"{idx2[1]+1},{idx2[0]+1},{dim_best}"


if __name__ == "__main__":

    part1, part2 = solution(9995)
    print(f"The largest total 3x3 square has a top-left corner of {part1}")
    print(f"The largest total nxn square has a top-left corner of {part2}")
