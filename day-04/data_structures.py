# Day 4: Python Data Structures
# Run from the project root: py .\day-04\data_structures.py

servers = ["web-01", "db-01", "web-01"]
target = ("web-01", 443)
unique_servers = set(servers)

status_by_host = {
    "web-01": "OK",
    "db-01": "WARNING",
}

# List: ordered collection that allows duplicates
print("Servers:", servers)
print("First server:", servers[0])

# Tuple: ordered collection that cannot be modified
print("Target:", target)

# Set: collection of unique values
print("Unique servers:", sorted(unique_servers))

# Dictionary: stores key-value pairs
print("Web server status:", status_by_host.get("web-01", "UNKNOWN"))
print("Database status:", status_by_host.get("db-01", "UNKNOWN"))
print("Missing host status:", status_by_host.get("api-01", "UNKNOWN"))
