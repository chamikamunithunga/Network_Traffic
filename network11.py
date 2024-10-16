import psutil
import time
from ping3 import ping
import platform

# Function to monitor bandwidth usage
def get_bandwidth_usage(interval=1):
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    
    time.sleep(interval)
    
    net_io = psutil.net_io_counters()
    bytes_sent_new = net_io.bytes_sent
    bytes_recv_new = net_io.bytes_recv
    
    upload_speed = (bytes_sent_new - bytes_sent) / (interval * 1024)  # KB/s
    download_speed = (bytes_recv_new - bytes_recv) / (interval * 1024)  # KB/s
    
    return upload_speed, download_speed

# Function to check network latency
def check_latency(host="8.8.8.8"):  # Google DNS server
    response_time = ping(host)
    if response_time is None:
        return "Packet Loss"
    else:
        return round(response_time * 1000, 2)  # ms

# Function to diagnose the network issues
def diagnose_issue(latency, upload_speed, download_speed):
    issue = None
    reason = ""
    solution_steps = []

    if isinstance(latency, str) and latency == "Packet Loss":
        issue = "Packet Loss"
        reason = "Packet loss may occur due to a poor connection or network congestion."
        solution_steps = [
            "Check the router and modem for proper functionality.",
            "Inspect network cables for damage.",
            "Restart the router and computer."
        ]

    elif latency > 150:
        issue = "High Latency"
        reason = "High latency can be caused by network congestion, long distance to the server, or low bandwidth."
        solution_steps = [
            "Reduce the number of devices using the network.",
            "Close any bandwidth-heavy applications (e.g., streaming or large downloads).",
            "If using Wi-Fi, try switching to a wired connection."
        ]

    # Check if speeds are below threshold
    if upload_speed < 1 or download_speed < 1:
        issue = "Slow Speeds"
        reason = "Slow speeds may result from limited bandwidth or network congestion."
        solution_steps.extend([
            "Limit the number of connected devices.",
            "Consider upgrading your internet plan if speeds are consistently low."
        ])

    return issue, reason, solution_steps

# Function to monitor network and provide diagnostics
def monitor_network(interval=5):
    while True:
        upload_speed, download_speed = get_bandwidth_usage(interval)
        latency = check_latency()

        print(f"Upload Speed: {upload_speed:.2f} KB/s")
        print(f"Download Speed: {download_speed:.2f} KB/s")
        print(f"Latency: {latency} ms")

        issue, reason, solution_steps = diagnose_issue(latency, upload_speed, download_speed)

        if issue:
            print(f"Issue Detected: {issue}")
            print(f"Reason: {reason}")
            print("Solution Steps:")
            for step in solution_steps:
                print(f"- {step}")

        print("-" * 30)  # Just for separating outputs
        time.sleep(interval)

if __name__ == "__main__":
    monitor_network()
