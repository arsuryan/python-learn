import json
import csv

with open('examples/holidays.json') as f:
    d = json.load(f)
    region_based_events = []
    for region, x in d.items():
        division = x.get("division")
        for event in x.get("events"):
            csv_dict = {"region": region, "division": division, "title": event.get("title"), "date": event.get("date")}
            region_based_events.append(csv_dict)

    keys = region_based_events[0].keys()
    with open('examples/holidays.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(region_based_events)