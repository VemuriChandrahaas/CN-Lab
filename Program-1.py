# Experiment 2: Write a program to identify your machine's host name and IP address

import socket

# Get the hostname of the machine
hostname = socket.gethostname()

# Get the IP address associated with the hostname
ip_address = socket.gethostbyname(hostname)

# Display the results
print("Hostname:", hostname)
print("IP Address:", ip_address)

# OUTPUT:
# Hostname: vm
# IP Address: 127.0.0.1
