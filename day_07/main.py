from string import ascii_uppercase as letters_all


def read_and_process(data_path: str):
    """
    Create two lists of dependent processes
    """

    before = []
    after = []
    f = open(data_path, "r")
    for x in f:
        before.append(x.strip().split()[1])
        after.append(x.strip().split()[7])
        
    return before, after


def update_lists(to_process, before, after, chars):
    """
    Updates all lists by removed characters
    """
    for c in chars:
        to_process = [a for a in to_process if a != c]
        after = [a for i, a in enumerate(after) if before[i] != c]
        before = [a for i, a in enumerate(before) if before[i] != c]
        
    return to_process, before, after


def part1(data_path="input"):
    """
    Creates the order of processes
    """
    before, after = read_and_process(data_path)
        
    # List of all tasks and output list
    to_process = sorted(list(set(after + before)))
    output = []
    
    while len(to_process) > 0:
        c = None
        for c in to_process:
            # Task is still dependent on others
            if c not in after:
                output.append(c)
                break
        
        # Proces one finished task
        to_process, before, after = update_lists(to_process, before, after, [c])
                
    return ''.join(output)
        

def finish_tasks(workers: dict, time: int):
    """
    When all workers utilized, finish the shortest tasks and remove them
    """
    time_needed = min(workers.values())
    finished = [k for k, v in workers.items() if v == time_needed]
    workers = {k: v - time_needed for k, v in workers.items() if v > time_needed}
    
    return time + time_needed, workers, finished
        
        
def part2(data_path="input", num_workers=5, min_time=61, letters=letters_all):
    """
    Calculate time needed to process the tasks
    """
    before, after = read_and_process(data_path)
    to_process = sorted(list(set(after + before)))
    workers = {}
    time = 0
    
    # Process tasks
    while len(to_process) > 0:
        # Assign tasks to workers with time needed to finish
        for c in to_process:
            if (c not in after) and (c not in workers):
                if len(workers) < num_workers:
                    workers[c] = min_time + letters.find(c)
                else:
                    break
                
        # Either runnable tasks were exhausted or no available worker
        time, workers, c = finish_tasks(workers, time)
        to_process, before, after = update_lists(to_process, before, after, c)
    
    return time


if __name__ == "__main__":

    print(f"Order of tasks to be completed is {part1()}")
    print(f"Time needed to finish the tasks is {part2()}")
