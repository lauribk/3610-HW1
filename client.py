import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            received_message = client_socket.recv(1024).decode('utf-8')
            if received_message:
                print(received_message)
            else:
                break
        except:
            break
    print("A server or connection error occured.")
    client_socket.close()

# Function to send messages to the server
def send_messages(client_socket):
    # menu for new users
    print("Type anything to chat.")
    print("Type '/private <username> <message>' to whisper.")
    print("Type '/quit' to exit.")

    while True:
        message = input()
        if message:
            if message == "/quit":
                break
            client_socket.send(message.encode('utf-8'))
    print("You have disconnected")
    client_socket.close()

def start_client(server_ip, server_port):
    #Create a TCP socket: client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connecting
    try:
        client_socket.connect((server_ip, server_port))
    except:
        print("There is no open server with that IP and port.")

    #Start a thread to listen for messages from the server
    threading.Thread(target = receive_messages , args = (client_socket,)).start()

    # Main thread sends messages
    client_socket.send(username.encode('utf-8'))
    send_messages(client_socket)

if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 12345

    print("Enter your username:")
    username = input()

    print("Enter the server IP:")
    SERVER_IP = str(input())

    print("Enter the server port number:")
    SERVER_PORT = int(input())

    try:
        start_client(SERVER_IP, SERVER_PORT)

    except:
        print("Invalid Server IP and port number.")

