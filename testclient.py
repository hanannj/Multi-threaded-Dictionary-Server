import socket

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 12345))

# Send a word to the server
word = input("Enter a word: ")
client_socket.send(word.encode())

# Receive the definition from the server
definition = client_socket.recv(1024).decode()

# Print the definition
print(definition)

# Close the socket
client_socket.close()


input()