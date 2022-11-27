

def read_and_process(data_path: str):
    """
    Initial state and mappings
    """

    f = open(data_path, "r")
    initial = None
    mapping = {}
      
    # Translate to binary information
    for x in f:
        if initial is None:
            initial = ['1' if c == '#' else '0' for c in x.strip().split()[2]]
        elif len(x.strip()) > 0:
            num = ''.join(['1' if c == '#' else '0' for c in x.strip().split()[0]])
            num = int(num, 2)
            bit = '1' if x.strip().split()[2] == '#' else '0'
            mapping[num] = bit
            
    return ''.join(initial), mapping


def fill_zeroes(state: str, pos_0: int):
    """
    Ad leading and trailing zeroes to string, modify position 0
    """
    # Leading zeroes
    if state[0] == '1':
        state = '0000' + state
        pos_0 += 2
    elif state[1] == '1':
        state = '000' + state
        pos_0 += 1
    elif state[2] == '1':
        state = '00' + state
    elif state[3] == '1':
        state = '0' + state
        pos_0 += -1
    else:
        pos_0 += -2
    
    # Trailing zeroes
    if state[-1] == '1':
        state = state + '0000'
    elif state[-2] == '1':
        state = state + '000'
    elif state[-3] == '1':
        state = state + '00'
    elif state[-4] == '1':
        state = state + '0'
    
    return state, pos_0


def assess_final(state: str, pos_0: int) -> int:
    """
    Calculate the final sum of all positions with plants
    """
    out = 0
    for bit in range(len(state)):
        if state[bit] == '1':
            out += bit - pos_0
            
    return out


def solution(iters, data_path="input"):
    """
    Generate state after iterations
    """
    state, maps = read_and_process(data_path)
    pos_0 = 0
    
    # Iterate through generations
    for it in range(iters):
        state, pos_0 = fill_zeroes(state, pos_0)
        state_part = ''
        for pos in range(len(state) - 4):
            num = int(state[pos:(pos+5)], 2)
            if num in maps:
                state_part += maps[num]
            else:
                state_part += '0'

        state = state_part
        
    return assess_final(state, pos_0)


if __name__ == "__main__":

    for i in [20, 5000, 50000, 500000]:
        print(f"Plants index sum after {i} iterations {solution(i)}")
