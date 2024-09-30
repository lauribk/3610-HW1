import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        #print all communications

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()
        #print all communications

def start_client(server_ip, server_port):
    #Create a TCP socket: client_socket

    #Start a thread to listen for messages from the server

    # Main thread sends messages
    #handle sending name
    send_messages(client_socket)

if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 12345

    print("Enter your username:")
    username = input()

    start_client(SERVER_IP, SERVER_PORT)

