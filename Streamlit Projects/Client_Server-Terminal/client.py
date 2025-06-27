import socket

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
host = '127.0.0.1'  # Localhost
port = 12345         # Same port as the server

# Connect to the server
client_socket.connect((host, port))

# Chat loop for communication
while True:
    # Send message to the server
    message = input("Client: ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'bye':
        print("Disconnected from the server.")
        break

    # Receive response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {response}")

# Close the connection
client_socket.close()
