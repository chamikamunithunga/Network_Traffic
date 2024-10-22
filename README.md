#01 Traffic Sniffer(traffic.py)
=================
Overview
------------
![SPVQOoGeJY3dccYNlH3zbMswiOvoBjda](https://github.com/user-attachments/assets/9eb692a5-ddd7-4fcc-9714-31852d155579)



This program is a simple network traffic sniffer that captures packets transmitted over the network for a specified website URL using Python's scapy library. It helps in monitoring network activity and can be useful for educational purposes, network diagnostics, or security analysis.

Features
----------
Captures packets transmitted to and from a specified website.
Displays the captured packets in real-time.
Runs on macOS and requires elevated permissions to access network interfaces.

#02 Network Performance Monitor (network11.py)
==============================

![Screenshot 2024-10-16 at 8 17 03 PM](https://github.com/user-attachments/assets/ec180dd2-0537-4d7b-bc54-7fe1a92af4a4)


A Python-based network performance monitoring tool that checks bandwidth usage, latency, and identifies potential network issues. This tool is useful for diagnosing slow network performance, packet loss, and other connectivity problems.

## Features
-----------

- Monitors upload and download speeds in real-time.
- Measures network latency to a specified host (default is Google's DNS server).
- Diagnoses network issues such as packet loss and high latency.
- Provides step-by-step solutions based on diagnosed issues.

## Requirements
----------------




#03 Network Monitoring Tool (network12.py)
=========================================

This is a Python-based network monitoring tool that captures network packets and scans specified IP addresses for open ports. It utilizes the Scapy library to sniff packets and checks for known malicious IP addresses.

## Features
------------

- **Packet Sniffing**: Captures network packets in real-time.
- **Malicious IP Detection**: Checks incoming packets against a predefined list of known malicious IP addresses.
- **Port Scanning**: Scans specified IP addresses for open ports within a specified range.


- Python 3.6 or higher
- `psutil` library for system and network information
- `ping3` library for pinging a host


#04 Network Bandwidth Calculator
==============================

This Python script calculates the download and upload bandwidth of your internet connection using the `speedtest-cli` library.

## Features
-----------

- Measures download speed in Mbps.
- Measures upload speed in Mbps.
- Retrieves the best server for testing based on ping.

#05 Location Tracking
======================
This application includes a location tracking feature that allows you to track the audio file's origin. The tracking data is represented by a unique number that corresponds to the geographical location of the audio source.

## How it Works
- When you upload an audio file, the application captures its geographical coordinates (latitude and longitude) based on the metadata embedded in the file (if available).
- A unique identifier is generated for each location, which can be used for mapping or tracking purposes.



