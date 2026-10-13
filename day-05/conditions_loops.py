# Day 5: Python Conditions and Loops
# Run from the project root: py .\day-05\conditions_loops.py

statuses = ["OK", "ERROR", "ERROR", "WARNING"]
error_count = 0

for status in statuses:
    if status == "ERROR":
        error_count += 1
        print("Error detected")
    elif status == "WARNING":
        print("Review warning")
    else:
        print("No error detected")

print(f"\nTotal errors: {error_count}")

# Practice: Categorize HTTP status codes using conditions and loops
status_codes = [200, 301, 404, 500, 204]

for code in status_codes:
    if 200 <= code < 300:
        category = "Success"
    elif 300 <= code < 400:
        category = "Redirect"
    elif 400 <= code < 600:
        category = "Client/server error"
    else:
        category = "Other or nonstandard code"

    print(f"HTTP {code}: {category}")
