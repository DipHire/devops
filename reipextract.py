import re

log_text = """ User login from 192.168.1.10
Database connection from 10.0.0.5
Failed attempt from 172.16.5.4
Another login from 10.23.5.9"""

ip_pattern = r'\d{1,3}(\.\d{1,3}){3}'


for m in re.finditer(ip_pattern, log_text):
    print(f"IP: {m.group():<15}")
    print(f"Start: {m.start()}  End: {m.end()}\n")


