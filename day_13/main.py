
def read_and_process(data_path: str):
    """
    Process and prepare input data
    """

    f = open(data_path, "r")
    out_map = []
    for x in f:
        out_map_tmp = [c for c in x]
        out_map.append(out_map_tmp)
    return out_map


def get_carts(data):
    """
    Get carts coordinates
    """
    
    carts = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] in ['>', '<', '^', 'v']:
                carts.append([r, c, data[r][c], 0])
                
    return carts
    

def fill_map(carts, data):
    """
    Makes map transparent - replaces carts with map elements
    """
    
    # Horizontal road
    for cart in carts:
        if cart[2] in ['<', '>']:
            data[cart[0]][cart[1]] = '-'
        else:
            data[cart[0]][cart[1]] = '|'
        
    return data
                        

def move_cart(cart, data):
    """
    Given map and cart position, move cart
    """
    
    # Helper maps
    pos_map = {'v': [1, 0], '^': [-1, 0], '<': [0, -1], '>': [0, 1]}
    cross_map = {'v': '>v<', '^': '<^>', '<': 'v<^', '>': '^>v'}
    turn_map = {'/':  {'^': '>', 'v': '<', '<': 'v', '>': '^'}, 
                '\\': {'^': '<', 'v': '>', '<': '^', '>': 'v'}}
    
    # Define new position
    cart[0] += pos_map[cart[2]][0]
    cart[1] += pos_map[cart[2]][1]
    
    # Define new direction
    char = data[cart[0]][cart[1]]
    if char == '+':
        cart[2] = cross_map[cart[2]][cart[3]]
        cart[3] = (cart[3] + 1) % 3
    elif char in ['/', '\\']:
        cart[2] = turn_map[char][cart[2]]
        
    return cart


def crash(cart, carts, pos):
    """
    Identify if there are crashes
    """
    for i, cart_other in enumerate(carts):
        if i != pos:
            if cart_other[:2] == cart[:2]:
                return i
    return -1


def part1(data_path="input"):
    """
    Move carts and find crash position
    """
    data = read_and_process(data_path)
    carts = get_carts(data)
    data = fill_map(carts, data)

    while True:
        # Sort carts to start with correct ones
        carts = sorted(carts, key=lambda x: (x[0], x[1]))
        for i, cart in enumerate(carts):
            cart = move_cart(cart, data)
            if crash(cart, carts, i) >= 0:
                return str(cart[1]) + ',' + str(cart[0])


def part2(data_path="input"):
    """
    Find the position of last remaining cart
    """
    data = read_and_process(data_path)
    carts = get_carts(data)
    data = fill_map(carts, data)
    
    while len(carts) > 1:
        # Sort carts to start with correct ones
        carts = sorted(carts, key=lambda x: (x[0], x[1]))
        to_remove = []
        
        # Generate new set of carts
        for i, cart in enumerate(carts):
            cart = move_cart(cart, data)
            crash_cart = crash(cart, carts, i)
            # Remember crashed carts
            if crash_cart >= 0:
                to_remove.append(i)
                to_remove.append(crash_cart)
        
        # Remove crashed carts
        carts = [c for i, c in enumerate(carts) if i not in to_remove]
        
    return str(carts[0][1]) + ',' + str(carts[0][0])


if __name__ == "__main__":

    print(f"Crash appeared at {part1()}")
    print(f"Last remaining non-crashed cart appeared at: {part2()}")
