import scapy.all as scapy
import requests
import threading

# Function to capture packets
def packet_sniffer():
    def packet_callback(packet):
        print(packet.summary())

    scapy.sniff(prn=packet_callback, store=False)

# Function to fetch the URL
def fetch_url(url):
    response = requests.get(url)
    print(f"\nResponse from {url}:")
    print(response.text[:200])  # Print the first 200 characters of the response

# Main function
def main():
    url = input("Enter the website URL: ")
    # Start the packet sniffer in a separate thread
    sniffer_thread = threading.Thread(target=packet_sniffer)
    sniffer_thread.daemon = True
    sniffer_thread.start()

    # Fetch the URL
    fetch_url(url)

    # Keep the script running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    main()
