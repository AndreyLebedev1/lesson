import selectors
import socket


selector = selectors.DefaultSelector()

def fibonacci(data):
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

def server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 9990))
    server_sock.listen()

    selector.register(
        fileobj=server_sock,
        events=selectors.EVENT_READ,
        data=accept_connection
    )


to_monitor = []


def accept_connection(server_sock: socket.socket) -> None:
    client_socket, client_addr = server_sock.accept()
    print(f'Connection has been received from {client_addr[0]}:{client_addr[1]}')
    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )


def send_message(client_sock: socket.socket) -> None:
    request = client_sock.recv(4096)
    print(f'Received: {request}')

    if request:
        print('Sending Fibonacci to client...')
        client_sock.send(str(fibonacci(int(request))).encode())
    else:
        print('Client has gone. Closing client socket...')
        selector.unregister(client_sock)
        client_sock.close()


def event_loop():
    while True:
        events = selector.select()  # key, events (bit mask read or write)
        for key, _ in events: # key has fileobj, events, data
            callback_function = key.data
            callback_function(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()