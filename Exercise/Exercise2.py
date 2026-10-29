accepted = 0
rejected = 0

info_count = 0
warn_count = 0
error_count = 0
server_errors = 0

total_latency = 0

while True:
    logs = input("Enter your log (or END): ").strip()

    # Stop processing
    if logs.upper() == "END":
        break

    # Ignore empty lines
    if logs == "":
        continue

    # Split the log into four fields
    parts = logs.split("|")

    if len(parts) != 4:
        print("Invalid input: expected four fields.")
        rejected += 1
        continue

    # Unpack the fields
    timestamp, level, status_text, latency_text = (
        part.strip() for part in parts
    )

    # Validate timestamp and log level
    level = level.upper()

    if timestamp == "" or level not in ("INFO", "WARN", "ERROR"):
        print("Invalid input: timestamp or level is invalid.")
        rejected += 1
        continue

    # Convert numeric fields
    try:
        status = int(status_text)
        latency = int(latency_text)
    except ValueError:
        print("Invalid input: status and latency must be integers.")
        rejected += 1
        continue

    # Validate numeric ranges
    if not (100 <= status <= 599) or latency < 0:
        print("Invalid input: status or latency is out of range.")
        rejected += 1
        continue

    # Update statistics only after the entire record is valid
    accepted += 1
    total_latency += latency

    if level == "INFO":
        info_count += 1
    elif level == "WARN":
        warn_count += 1
    elif level == "ERROR":
        error_count += 1

    if 500 <= status <= 599:
        server_errors += 1

# Calculate average latency safely
if accepted > 0:
    average_latency = total_latency / accepted
    average_display = f"{average_latency:.2f} ms"
else:
    average_display = "N/A (no accepted records)"

# Print final report
print("\n========== SERVER LOG REPORT ==========")
print(f"Accepted records:   {accepted}")
print(f"Rejected records:   {rejected}")
print(f"INFO records:       {info_count}")
print(f"WARN records:       {warn_count}")
print(f"ERROR records:      {error_count}")
print(f"HTTP 5xx responses: {server_errors}")
print(f"Average latency:    {average_display}")