import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = '127.0.0.1'  # Localhost
port = 12345         # Port to bind the server

# Bind the socket to the address and port
server_socket.bind((host, port))

# Listen for incoming connections (max 5 connections in the queue)
server_socket.listen(5)
print("Server listening on", host, ":", port)

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print("Connection from", client_address)

# Chat loop for communication
while True:
    # Receive message from client
    message = client_socket.recv(1024).decode('utf-8')
    
    if message.lower() == 'bye':
        print("Client has disconnected.")
        break
    
    print(f"Client: {message}")

    # Send response to client
    response = input("Server: ")
    client_socket.send(response.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()
