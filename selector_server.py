import socket
from select import select

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
    server_sock.bind(('localhost', 9990))
    server_sock.listen()

    return server_sock


to_monitor = []


def accept_connection(server_sock: socket.socket) -> None:
    client_socket, client_addr = server_sock.accept()
    print(f'Connection has been received from {client_addr[0]}:{client_addr[1]}')
    to_monitor.append(client_socket)


def send_message(client_sock: socket.socket) -> None:
    request = client_sock.recv(4096).decode()
    print(f'Received: {request}')

    if request:
        print('Sending Fibonacci to client...')
        client_sock.send(str(fibonacci(int(request))).encode())
    else:
        print('Client has gone. Closing client socket...')
        to_monitor.remove(client_sock)
        client_sock.close()

def event_loop():
    while True:
        # readable, writable, errors
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock == server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    server_socket = get_server_socket()
    to_monitor.append(server_socket)
    event_loop()