from typing import final
import pandas as pd
import csv

star_data = []

with open("star_with_gravity.csv") as f:
    reader = csv.reader(f)
    for data in reader:
        star_data.append(data)
        
star_headers = star_data[0]
star_data_rows = star_data[1:]

final_data = []

for star_data in star_data_rows:
    temp_dict = {
        "name": star_data[1],
        "Distance": star_data[2],
        "Mass": star_data[3],
        "Radius": star_data[4],
        "Gravity": star_data[9]
    }

    final_data.append(temp_dict)
    
print(final_data)