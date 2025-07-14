with open("content.txt", "r") as file:
    lines = file.readlines()

today_events = []

i = 0
while i < len(lines):
    if "TODAY" in lines[i]:
        event_name = lines[i].strip()
        event_name_parts = lines[i].strip().split()

        event_name = " ".join(event_name_parts[:-1])
        
        event_time = lines[i + 2].strip()
        
        event_location = lines[i + 4].strip()

        today_events.append(f"Event: {event_name}\nTime: {event_time}\nPlace: {event_location}\n")
        
    i += 1

with open("eventcredential.txt", "w") as outfile:
    for event in today_events:
        outfile.write(event + "\n")