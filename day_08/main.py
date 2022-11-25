
def read_and_process(data_path: str):
    """
    Create list of input integers
    """

    f = open(data_path, "r")
    out = None
    for x in f:
        out = [int(c) for c in x.strip().split()]
    return out


def get_metadata_sum(tree: list, metadata_sum: int):
    """
    Calculate the sum of metadata
    """
    nodes = tree.pop(0)
    meta = tree.pop(0)
    for i in range(nodes):
        tree, metadata_sum = get_metadata_sum(tree, metadata_sum)
    for i in range(meta):
        metadata_sum += tree.pop(0)
    return tree, metadata_sum


def part1(data_path="input"):
    """
    Calculate the sum of metadata and process data
    """
    tree = read_and_process(data_path)
        
    return get_metadata_sum(tree, 0)[1]


def get_child_sum(tree: list):
    """
    Calculate the sum of metadata of children
    """
    nodes = tree.pop(0)
    metas = tree.pop(0)
    child_metas = []
    out = 0
    for i in range(nodes):
        tree, child_meta = get_child_sum(tree)
        child_metas.append(child_meta)
    for i in range(metas):
        val = tree.pop(0)
        if nodes == 0:
            out += val
        elif val <= nodes:
            out += child_metas[val - 1]
        
    return tree, out


def part2(data_path="input"):
    """
    Calculate the sum of metadata and process data
    """
    tree = read_and_process(data_path)
        
    return get_child_sum(tree)[1]


if __name__ == "__main__":

    print(f"Sum of metadata is {part1()}")
    print(f"Sum of child metadata is {part2()}")
