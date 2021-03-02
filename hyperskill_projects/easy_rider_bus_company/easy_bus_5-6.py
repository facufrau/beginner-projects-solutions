# Stage 5-6 Easy Rider Bus Company 
from datetime import time
import json

def convert_time(time_str):
    """Converts a time string to a time object."""
    time_data = [int(x) for x in time_str.split(":")]
    hours, minutes = time_data[0], time_data[1]
    return time(hours, minutes)
    
def main():
    data = json.loads(input())
    # Dictionary for storing bus_id and status for time schedules.
    status = {}
    
    # Parse data and store it to a dictionary, with bus id as key,
    # and a list of tuples as values ex: {bus_id: [(time1, name1), (time2, name2)]}
    lines = {}
    for item in data:
        bus_id= item["bus_id"]
        a_time = convert_time(item["a_time"])
        name = item["stop_name"]
        if bus_id not in lines:
            lines[bus_id] = []
        lines[bus_id].append((a_time, name))
    
    # print(lines)
    # {512: [(datetime.time(8, 13), 'Bourbon Street'), (datetime.time(8, 16), 'Sunset Boulevard')]}
    
    for line, data in lines.items():
        status[line] = []
        for i, j in zip(data, data[1:]):
            #i:(datetime.time(8, 13), 'Bourbon Street'), j:(datetime.time(8, 16), 'Sunset Boulevard')
            curr_time = i[0]
            next_time = j[0]
            next_name = j[1]
            if curr_time > next_time:
                status[line].append(next_name) 
                break
    
    # Print final results with given formatting.
    print("Arrival time test:")
    if all(value == [] for value in status.values()):
        print("OK")
    else:
        for line, error in status.items():
            if error != []:
                print(f"bus_id line {line}: wrong time on station {error[0]}")
        
    
main()