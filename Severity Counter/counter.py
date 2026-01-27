severity_count = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

with open("log.txt", "r") as file:
    for line in file:
        if line.startswith("INFO"):
            severity_count["INFO"] += 1
        elif line.startswith("WARNING"):
            severity_count["WARNING"] += 1
        elif line.startswith("ERROR"):
            severity_count["ERROR"] += 1

print("Log Severity Summary")
print(f"INFO: {severity_count['INFO']}")
print(f"WARNING: {severity_count['WARNING']}")
print(f"ERROR: {severity_count['ERROR']}")
