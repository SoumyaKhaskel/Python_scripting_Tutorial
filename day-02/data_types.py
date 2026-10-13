hostname = "web-01"
port = 443
response_time = 0.28
reachable = True

print(f"Hostname: {hostname} ({type(hostname).__name__})")
print(f"Port: {port} ({type(port).__name__})")
print(f"Response time: {response_time} ({type(response_time).__name__})")
print(f"Reachable: {reachable} ({type(reachable).__name__})")

raw_attempts = input("Enter the number of attempts: ")

try:
    attempts = int(raw_attempts)

    if attempts < 0:
        raise ValueError("Attempts cannot be negative.")

except ValueError as error:
    print(f"Invalid input: {error}")

else:
    print(f"Attempts recorded: {attempts}")
