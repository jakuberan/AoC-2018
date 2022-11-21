from datetime import datetime
import numpy as np


def parse_line(line: str):
    """
    Return a date of action additional info
    """
    
    date = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
    if line[-2:] == 'ep':
        info = 'sleep'
    elif line[-2:] == 'up':
        info = 'up'
    else:
        info = int(line.split()[3].replace('#', ''))
    
    return date, info


def id_for_max_minute(tracker: dict) -> int:
    """
    Return ID * minute for ID for which the max minute was recorded
    """
    max_minute = 0
    argmax_minute = None
    max_guard = None
    
    for guard in tracker.keys():
        if max(tracker[guard]) > max_minute:
            max_minute = max(tracker[guard])
            argmax_minute = np.argmax(tracker[guard])
            max_guard = guard
            print(f'New max {max_minute} achieved in guard {guard} for minute {argmax_minute}')
            
    return max_guard * argmax_minute
    

def solution_to_both(data_path="input"):
    """"
    Apply strategy 1 and then 2
    """
    # Create guard info dict
    all_info = {}
    guard_info = {}
    
    # Parse input data
    f = open(data_path, "r")
    for x in f:
        date, info = parse_line(x.strip())
        all_info[date] = info
        
    # Process times asleep for each guard
    guard = None
    date_sleep = None
    minute_sleep = None
    for date in sorted(all_info.keys()):
        info = all_info[date]
        if type(info) == int:
            guard = info
            if guard not in guard_info.keys():
                guard_info[guard] = 0
        elif info == 'sleep':
            date_sleep = date
        else:
            guard_info[guard] += (date - date_sleep).seconds / 60

    # Find guard with most minutes asleep
    max_guard = max(guard_info, key=guard_info.get)
    
    # Init minute tracker
    minute_tracker = {}
    for guard in guard_info.keys():
        minute_tracker[guard] = np.zeros(60)
        
    # Count minutes asleep
    for date in sorted(all_info.keys()):
        info = all_info[date]
        if type(info) == int:
            guard = info
        elif info == 'sleep':
            minute_sleep = date.minute
        else:
            minute_up = date.minute
            if minute_up >= minute_sleep:
                minute_tracker[guard][minute_sleep:minute_up] += 1
            else:
                minute_tracker[guard][:minute_up] += 1
                minute_tracker[guard][minute_sleep:] += 1

    return np.argmax(minute_tracker[max_guard]) * max_guard, id_for_max_minute(minute_tracker)


if __name__ == "__main__":
    
    sol1, sol2 = solution_to_both()

    print(f"Solution for parth 1: {sol1}")
    print(f"Solution for parth 2: {sol2}")
