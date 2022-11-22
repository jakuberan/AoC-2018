import string


def react(polymer: str) -> str:
    """
    Perform polymer reaction
    """
    polymer_list = list(polymer)
    
    # React the polymer
    polymer_new = [polymer_list.pop()]
    while len(polymer_list) > 0:
        char = polymer_list.pop()
        if (char.lower() == polymer_new[0].lower()) and (char != polymer_new[0]):
            polymer_new.pop(0)
        else:
            polymer_new.insert(0, char)
            
    return ''.join(polymer_new)


def solution(data_path="input"):
    """"
    Calculates length of polymer after reaction and also all possible removals
    """

    f = open(data_path, "r")
    polymer = None
    for x in f:
        polymer = x.strip()
        
    # Perform basic polymer reaction
    polymer = react(polymer)
    min_length_1 = len(polymer)
        
    # Find minimum length after considering all removals
    min_len = min_length_1
    for char in string.ascii_lowercase:
        polymer_temp = polymer
        polymer_temp = polymer_temp.replace(char, '').replace(char.upper(), '')
        min_len = min(min_len, len(react(polymer_temp)))
    
    return min_length_1, min_len


if __name__ == "__main__":
    
    sol1, sol2 = solution()

    print(f"Length of shortened polymer is {sol1}")
    print(f"Length of shortest polymer after removal is {sol2}")
