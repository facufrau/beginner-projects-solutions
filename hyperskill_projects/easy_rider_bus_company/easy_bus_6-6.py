# Stage 6-6 Easy Rider Bus Company 
from collections import Counter
import json

def parse_stops(json_data):
    """Parse the input and convert to dictionaries of stop types"""
    stops_names = {"start": [], "finish": [], "other": [], "on demand": []}
    for item in json_data:
        # Cache data for easier reading
        bus_id = item["bus_id"]
        stop_type = item["stop_type"]
        stop_name = item["stop_name"]
        
        # Add the stop names and bus id to a dict of dicts.
        if stop_type == "S":
            stops_names["start"].append(stop_name)
        elif stop_type == "F":
            stops_names["finish"].append(stop_name) 
        else:
            if stop_type == "O":
                stops_names["on demand"].append(stop_name)
            else:
                stops_names["other"].append(stop_name)
    return stops_names

def main():
    data = json.loads(input())
    stops_names = parse_stops(data)

    # Create lists that will contain the stops name parsed before.
    start_stops = []
    finish_stops = []
    ondemand_stops = []
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
        
        elif stop_type == 'on demand':
            for name in names:
                if name not in ondemand_stops:
                    ondemand_stops.append(name)
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
    
    # Create a list with all the stops that can not be ondemand.
    special_stops = start_stops + finish_stops + transfer_stops
    print("On demand stops test:")
    if all(stop not in special_stops for stop in ondemand_stops):
        print("OK")
        return 0
    
    # If at least 1 ondemand stop is wrong create a list and print results.
    wrong_types = []
    for stop in ondemand_stops:
        if stop in special_stops:
            wrong_types.append(stop)
    print("Wrong stop type: ", sorted(wrong_types))
        

main()
