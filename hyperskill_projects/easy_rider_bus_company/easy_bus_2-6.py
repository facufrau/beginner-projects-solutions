# Easy bus rider company - Stage 2-6
import json
import re
          
def check_format(element, errors_dict):
    """ Checks formatting in the fields required for each element."""
    
    # Check stop name format
    name_re = r"([A-Z][a-z]+\s)+(Road|Avenue|Boulevard|Street)$"
    name = re.match(name_re, element["stop_name"])
    if not name:
        errors_dict["stop_name"] += 1
    
    # Check stop type format
    valid_types = ["S", "O", "F", ""]
    if element["stop_type"] not in valid_types:
        errors_dict["stop_type"] += 1
    
    # Check arrival time format (HH:MM 24hour)
    time_re = r"(([01]{1}\d|[2]{1}[0-4]):[0-5]{1}\d{1})"
    time_result = re.match(time_re, element["a_time"])
    if not time_result or len(element["a_time"]) > 5:
        errors_dict["a_time"] += 1
    
    return 0
    
errors = {"stop_name": 0, "stop_type": 0, "a_time": 0 }
data = json.loads(input())
for item in data:
    check_format(item, errors)
total = sum(errors.values())

print(f"Format validation: {total} errors")
for key, value in errors.items():
    print(f"{key}: {value}")
