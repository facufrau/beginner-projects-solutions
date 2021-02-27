# Easy bus rider company - Stage 1-6
import json

data = json.loads(input())
errors = { "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0 }
           
def check_fields(element, errors_dict):
    """ Checks all fields and data type for each element."""
    if not element["bus_id"] or not isinstance(element["bus_id"], int):
        errors_dict["bus_id"] += 1
        
    if not element["stop_id"] or not isinstance(element["stop_id"], int):
        errors_dict["stop_id"] += 1
        
    if not element["stop_name"] or not isinstance(element["stop_name"], str):
        errors_dict["stop_name"] += 1
        
    if element["next_stop"] == "" or not isinstance(element["next_stop"], int):
        errors_dict["next_stop"] += 1
          
    if element["stop_type"]:
        if not isinstance(element["stop_type"], str):
            errors_dict["stop_type"] += 1
        elif len(element["stop_type"]) > 1:
            errors_dict["stop_type"] += 1    

    if isinstance(element["a_time"], str):
        if len(element["a_time"]) != 5:
            errors_dict["a_time"] += 1 
    else:
        errors_dict["a_time"] += 1
            
    return 0

for item in data:
    check_fields(item,errors)
total = sum(errors.values())

print(f"Type and required field validation: {total} errors")
for key, value in errors.items():
    print(f"{key}: {value}")