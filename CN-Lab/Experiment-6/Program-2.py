# Experiment 6: Applications using TCP sockets (File Transfer)
# Program 2: Source Code (File Client)

import socket


def file_transfer_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    filename = input("Enter the filename to send: ")
    client_socket.sendall(filename.encode())

    # Wait for the server's acknowledgement before sending the file data
    client_socket.recv(1024)

    try:
        with open(filename, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                client_socket.sendall(chunk)
        print(f"File {filename} sent successfully.")
    except FileNotFoundError:
        print(f"File {filename} not found.")

    client_socket.close()


if __name__ == '__main__':
    file_transfer_client()

# OUTPUT:
# Enter the filename to send: test.txt
# File test.txt sent successfully.
