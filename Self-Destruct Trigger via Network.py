import socket
import sys

def start_server(port, usb_drive_letter):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)

    print(f"Listening for remote activation on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")
        
        # Receive self-destruct command
        command = client_socket.recv(1024).decode()
        if command == "SELF_DESTRUCT":
            print("Remote self-destruct triggered.")
            # Execute the self-destruct action here
            self_destruct(usb_drive_letter)
            client_socket.sendall(b"Self-destruct complete.")
        client_socket.close()

def self_destruct(drive_letter):
    # Execute your destructive actions here
    # For example: Deleting files or disabling the USB
    print(f"Initiating self-destruct on {drive_letter}:")
    os.system(f"del /f /q {drive_letter}:\\*.*")  # Deletes all files in the drive
    os.system(f"format {drive_letter}: /Q /Y")  # Quick format the USB drive

if __name__ == "__main__":
    port = 12345  # Port to listen on
    usb_drive_letter = 'E'  # Replace with actual drive letter
    start_server(port, usb_drive_letter)
