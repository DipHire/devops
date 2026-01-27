from datetime import datetime

with open("build_time.txt", "r") as file:
    lines = file.readlines()

start_time_str = lines[0].split(": ")[1].strip()
end_time_str = lines[1].split(": ")[1].strip()

start_time = datetime.strptime(start_time_str, "%H:%M")
end_time = datetime.strptime(end_time_str, "%H:%M")

duration = end_time - start_time

total_minutes = duration.seconds // 60

print(f"Total Build Time: {total_minutes} minutes")
