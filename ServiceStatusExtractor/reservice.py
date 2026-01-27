import re

pattern = r'(Starting|Started|Failed)\s+([\w.-]+\.service)'

with open("log.txt", "r") as file:
    for log in file:
        match = re.search(pattern, log)
        if match:
            status, service = match.groups()
            print(f"Service: {service} | Status: {status}")
