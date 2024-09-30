import socket
import threading

# Global list to keep track of connected clients
clients = []

# Function to handle communication with each client
def handle_client(client_socket, client_address):
    #receive username
    username = client_socket.recv(1024).decode("utf-8")

    #changed format to match example output
    print(f"[{username} connected] Total clients: {len(clients)}")
    client_socket.send(f"Welcome to the chat, {username}!".encode('utf-8'))

    while True:
        #receive the message
        message = client_socket.recv(1024).decode("utf-8")
        #check to see if it is a special menu option
        if message == "/quit":
            break
        #elif message == "/private":
        elif message:
            broadcast(f"[{username}]: {message}", client_socket)
    # deal with disconnection
    remove_client(client_socket)
    print(f"[{username} disconnected] Total clients: len(clients)")
        

# Function to broadcast messages to all clients
def broadcast(message, sender_socket):
    # also print messages to server terminal
    print(message)

    #sending to all clients
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        #in case the client has disconnected due to a server connection error
        except:
            remove_client(client)

# Fucntion to remove a client from the list and close the connection
def remove_client(client_socket):
    if client_socket in clients:
        #closing the socket and removing them from the client list
        client_socket.close()
        clients.remove(client_socket)

def start_server(server_ip, server_port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))

    #Handle multiple clients simultaneously
    server_socket.listen(5)

    print(f"[SERVER STARTED] Listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        #Start a new thread to handle the client
        threading.Thread(target = handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 12345
    start_server(SERVER_IP, SERVER_PORT)