import socket

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server's IP address
server_ip = input('Enter the server IP address: ')

while True:
  # Connect to the server
  client_socket.connect((server_ip, 5000))

  # Get a guess from the user
  guess = input('Enter a number between 1 and 100: ')
  guess = int(guess)

  # Send the guess to the server
  client_socket.send(bytes(str(guess), 'utf-8'))

  # Receive the response from the server
  data = client_socket.recv(1024)

  # Check if the guess was correct
  if data == b'You guessed correctly!':
    print('You guessed correctly!')
    break
  else:
    print('You guessed incorrectly. Try again.')

# Close the client socket
client_socket.close()


