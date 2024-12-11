import socket

def send_trigger(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send self-destruct command
    client_socket.sendall(b"SELF_DESTRUCT")

    # Receive confirmation
    response = client_socket.recv(1024)
    print(f"Server Response: {response.decode()}")
    client_socket.close()

if __name__ == "__main__":
    host = '192.168.1.100'  # IP of the laptop where server is running
    port = 12345  # Port number used by the server
    send_trigger(host, port)
