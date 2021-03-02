# Stage 4-6 Easy Rider Bus Company 
from collections import Counter
import json

def parse_stops(json_data):
    """Parse the input and convert to 2 dictionaries."""
    lines_stops = {}
    stops_names = {"start": [], "finish": [], "other": []}
    for item in json_data:
        # Cache data for easier reading
        bus_id = item["bus_id"]
        stop_type = item["stop_type"]
        stop_name = item["stop_name"]
        
        # Add the stop type to a dictionary of lists with bus_id as key.
        lines_stops.setdefault(bus_id, [])
        lines_stops[bus_id].append(stop_type)
        
        # Add the stop names and bus id to a dict of dicts.
        if stop_type == "S":
            stops_names["start"].append(stop_name)
        elif stop_type == "F":
            stops_names["finish"].append(stop_name)
        else:
            stops_names["other"].append(stop_name)
    return lines_stops, stops_names

def main():
    data = json.loads(input())
    lines_stops, stops_names = parse_stops(data)

    # Check if all lines have a starting and ending stop
    for line, stops in lines_stops.items():
        if "S" not in stops or "F" not in stops:
            print(f"There is no start or end stop for the line: {line}.")
            return 1

    # Create lists that will contain the stops name parsed before.
    start_stops = []
    finish_stops = []
    all_stops = []
    
    # Iterate over the stops names and save in three list.
    # One for starting stops, one for finish.
    # The last list contains all the stops names for checking transfers later.
    for stop_type, names in stops_names.items():
        if stop_type == 'start':
            for name in names:
                if name not in start_stops:
                    start_stops.append(name)
                all_stops.append(name)

        elif stop_type == 'finish':
            for name in names:
                if name not in finish_stops:
                    finish_stops.append(name)
                all_stops.append(name)
        else:
            for name in names:
                all_stops.append(name)
    
    # Check for repeated stops in all stops list and add to transfers stops.
    # A repeated name in all stops means that is shared between two stops
    transfer_stops = []
    for stop in all_stops:
        if stop not in transfer_stops and all_stops.count(stop) > 1:
            transfer_stops.append(stop) 
    
    # Print final results       
    print(f"Start stops: {len(start_stops)}", sorted(start_stops))
    print(f"Transfer stops: {len(transfer_stops)}", sorted(transfer_stops))
    print(f"Finish stops: {len(finish_stops)}", sorted(finish_stops))
    
main()
