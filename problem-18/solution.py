from collections import Counter

# Set the correct file name
log_file_path = 'Description.txt'

# Create a Counter to store IP counts
ip_counter = Counter()

# Open and read the log file line by line
with open(log_file_path, 'r') as file:
    for line in file:
        # Strip whitespace and check if line is not empty
        parts = line.strip().split()
        if len(parts) < 1:
            continue  # Skip empty or malformed lines
        
        ip = parts[0]
        ip_counter[ip] += 1

# Get the top 3 IPs with most requests
top_ips = ip_counter.most_common(3)

# Print the results
print("Top 3 IPs with the most requests:")
for ip, count in top_ips:
    print(f"{ip}: {count} requests")
