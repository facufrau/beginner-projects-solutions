# Easy Rider Bus Company - Stage 3-6
from collections import Counter
import json
import re
  
buses = {}
data = json.loads(input())
for item in data:
    buses.setdefault(item["bus_id"], 0)
    buses[item["bus_id"]] += 1
    
print("Line names and number of stops:")
for line, stops in buses.items():
    print(f"bus_id: {line}, stops: {stops}")
    
