import socket
import time

SERVER_HOST = 'localhost'
SERVER_PORT = 9999


client_socket = socket.socket()
client_socket.connect((SERVER_HOST, SERVER_PORT))


print('Input number:')
input = input()
t0 = time.time()
for n in range(1, int(input)+1):
    client_socket.send(str(n).encode())
    response = client_socket.recv(4096)
    print(f'{response} was received')
    #time.sleep(0)
t1 = time.time()
print(f'timestep = {t1-t0},usin port: {SERVER_PORT}')
print('Closing connection...')
client_socket.close()