import random
import socket

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))  # Listen on all available interfaces
server_socket.listen()

# Generate a random number for the client to guess
secret_number = random.randint(1, 100)

while True:
  # Accept incoming connections
  client_socket, client_address = server_socket.accept()

  # Receive data from the client
  data = client_socket.recv(1024)
  data = int(data)

  # Check if the received data is the secret number
  if data == secret_number:
    # Send a message back to the client to let them know they guessed correctly
    client_socket.send(b'You guessed correctly!')
  else:
    # Send a message back to the client to let them know they guessed incorrectly
    client_socket.send(b'You guessed incorrectly. Try again.')

  # Close the client socket
  client_socket.close()


