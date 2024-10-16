import speedtest

def calculate_bandwidth():
    try:
        st = speedtest.Speedtest()
        print("Retrieving best server...")
        st.get_best_server(timeout=10)  # Adjust timeout as needed
        print("Running download test...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        print("Running upload test...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    calculate_bandwidth()
