import numpy as np


def process_coord(line: str) -> list:
    """
    Return coordinates given by input line
    """
    y, x = line.split(',')
    
    return [int(x), int(y)]


def check_coordinates(crd, x, y, areas_shape):
    """
    Check if a neighbor is still a valid cell in areas
    """
    if crd[0] + x == areas_shape[0]:
        return False
    elif crd[0] + x < 0:
        return False
    elif crd[1] + y == areas_shape[1]:
        return False
    elif crd[1] + y < 0:
        return False
    else:
        return True


def update_areas(crd, x, y, stack_crd, areas, steps, mark=100):
    """
    Update areas, steps and stack by a cell neighbor
    """
    
    if check_coordinates(crd, x, y, areas.shape):
        
        crd_x = crd[0] + x
        crd_y = crd[1] + y
        idx = areas[crd[0], crd[1]]
        step = steps[crd[0], crd[1]]
        # Neighbour was not used
        if areas[crd_x, crd_y] == 0:
            stack_crd.append([crd_x, crd_y])
            areas[crd_x, crd_y] = idx
            steps[crd_x, crd_y] = step + 1
        # Neighbor was already used by a different center within the same number of steps
        elif (areas[crd_x, crd_y] < 0) and (areas[crd_x, crd_y] != idx):
            if steps[crd_x, crd_y] == step + 1:
                areas[crd_x, crd_y] = mark

    return stack_crd, areas, steps


def get_max_finite_area(areas, coords):
    """"
    Calculates max finite area
    """
    # Eliminate infinite areas
    max_fin_area = 0
    for i in range(len(coords)):
        if (i + 1) not in areas[0, :]:
            if (i + 1) not in areas[:, 0]:
                if (i + 1) not in areas[areas.shape[0] - 1, :]:
                    if (i + 1) not in areas[:, areas.shape[1] - 1]:
                        area = sum(sum(areas == (i + 1)))
                        max_fin_area = max(max_fin_area, area)
                        
    return max_fin_area
    

def part1(data_path="input") -> int:
    """"
    Expands areas and identifies the largest finite one
    """
    
    # Assemble list of coordinates
    coords = []
    f = open(data_path, "r")
    for x in f:
        coords.append(process_coord(x.strip()))
    coords = np.array(coords)
    
    # Bring coordinates to zero
    coords[:, 0] -= min(coords[:, 0])
    coords[:, 1] -= min(coords[:, 1])
    
    # Initialize areas and stack
    areas = np.zeros([max(coords[:, 0]) + 1, max(coords[:, 1]) + 1])
    steps = np.zeros([max(coords[:, 0]) + 1, max(coords[:, 1]) + 1])
    stack_crd = []
    for i in range(len(coords)):
        areas[coords[i][0], coords[i][1]] = -(i + 1)
        steps[coords[i][0], coords[i][1]] = 1
        stack_crd.append([coords[i][0], coords[i][1]])
        
    # Iterate through stack
    while len(stack_crd) > 0:
        crd = stack_crd.pop(0)
        if areas[crd[0], crd[1]] < 0:
            # search for unused neighbors
            stack_crd, areas, steps = update_areas(crd,  1,  0, stack_crd, areas, steps)
            stack_crd, areas, steps = update_areas(crd, -1,  0, stack_crd, areas, steps)
            stack_crd, areas, steps = update_areas(crd,  0,  1, stack_crd, areas, steps)
            stack_crd, areas, steps = update_areas(crd,  0, -1, stack_crd, areas, steps)
            # Update areas
            areas[crd[0], crd[1]] = -areas[crd[0], crd[1]]
                        
    return get_max_finite_area(areas, coords)


def part2(data_path="input", limit=10000) -> int:
    """"
    Finds all cell within 10000 steps from all centers 
    """
    
    # Assemble list of coordinates
    coords = []
    f = open(data_path, "r")
    for x in f:
        coords.append(process_coord(x.strip()))
    coords = np.array(coords)
    
    # Bring coordinates to zero
    coords[:, 0] -= min(coords[:, 0])
    coords[:, 1] -= min(coords[:, 1])
    
    # Initialize areas and stack
    coord_r = np.zeros([max(coords[:, 0]) + 1, max(coords[:, 1]) + 1])
    coord_c = np.zeros([max(coords[:, 0]) + 1, max(coords[:, 1]) + 1])
    
    # Arrays of row and col coordinates
    for r in range(coord_r.shape[0]):
        for c in range(coord_r.shape[1]):
            coord_r[r, c] = r
            coord_c[r, c] = c

    # Return distance from each center
    steps_sum = np.zeros([max(coords[:, 0]) + 1, max(coords[:, 1]) + 1])
    for crd in coords:
        steps_sum += np.abs(coord_r - crd[0])
        steps_sum += np.abs(coord_c - crd[1])
        
    return sum(sum(steps_sum < limit))
        

if __name__ == "__main__":
    
    print(f"Max finite area is {part1()}")
    print(f"There are {part2()} cell within 10000 steps from all centers")
