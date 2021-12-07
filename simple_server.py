import socket


def fibonacci(data):
    data-=2
    fib1 = 1
    fib2 = 1
    while data > 0:
        fib1, fib2 = fib2, fib1 + fib2
        data -= 1
    return fib2
    #if data in (1, 2):
    #    return 1
    #print(data)
    #return fibonacci(data - 1) + fibonacci(data - 2)


def get_server_socket():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 9999))
    server_sock.listen()

    return server_sock


server_socket = get_server_socket()

while True:
    print('Waiting new connection...')
    client_socket, client_addr = server_socket.accept()
    print(f'Connection has been received from {client_addr[0]}:{client_addr[1]}')

    while True:
        data = client_socket.recv(4096).decode()
        print(f'Received: {data}')

        if data:
            #print('Sending Ping to client...')
            print('Sending Number of Fibonacci to client...')
            client_socket.send(str(fibonacci(int(data))).encode())
        else:
            print('Client has gone. Closing client socket...')
            client_socket.close()
            break
