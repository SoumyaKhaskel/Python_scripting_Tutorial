# Day 3: Python Strings and Formatting
# Run from the project root: py .\day-03\strings.py

raw_status = "  ERROR: Login Failed  "
clean_status = raw_status.strip().lower()
hostname = "web-01"

print(f"Host={hostname} | Status={clean_status}")

cpu_usage = 82.456
print(f"CPU usage: {cpu_usage:.1f}%")

sample = "Python scripting is useful"

print(sample.upper())
print(sample.replace("useful", "practical"))
print(sample.split())
