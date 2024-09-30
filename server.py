import socket
import threading

# Global list to keep track of connected clients
clients = []

# Function to handle communication with each client
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    client_socket.send("Welcome to the chat server!\n".encode('utf-8'))

    while True:
        pass

# Function to broadcast messages to all clients
def broadcast(message, sender_socket):
    for client in clients:
        pass

# Fucntion to remove a client from the list and close the connection
def remove_client(client_socket):
    if client_socket in clients:
        pass

def start_server(server_ip, server_port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))

    #Handle multiple clients simultaneously

    print(f"[SERVER STARTED] Listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        #Start a new thread to handle the client

if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 8080
    start_server(SERVER_IP, SERVER_PORT)