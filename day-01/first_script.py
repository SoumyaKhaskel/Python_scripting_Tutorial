from datetime import datetime

task_name = "daily system check"

print(f"Starting: {task_name}")
print(f"Time: {datetime.now():%Y-%m-%d %H:%M:%S}")
print("Task completed.")
