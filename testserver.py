import socket
import threading
import json


try:
    DICTIONARY_FILE = open("dictionary.json", 'r').read()
    dictionary = json.loads(DICTIONARY_FILE)

except FileNotFoundError:
    print("Dictionary file not found.")


# Define the thread function to handle client requests
def handle_client(client_socket):
    try:
        # Receive the word from the client
        data = client_socket.recv(1024)
        if not data:
            raise Exception("No data received from client.")
        word = data.decode().strip()

        # Send the definition back to the client
        client_socket.send(dictionary[word].encode())

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the socket
        client_socket.close()

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
# Bind the server socket to a port
server_socket.bind(("localhost", 12345))

# Listen for incoming connections
server_socket.listen()
print('Server started on {}:{}'.format(*server_address))

# Main loop to handle incoming connections
while True:
    try:
        # Accept a new client connection
        client_socket, address = server_socket.accept()
        print('Client connected from {}:{}'.format(*address))
        # Spawn a new thread to handle the client request
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()
    except Exception as e:
        print(f"Error occurred: {e}")