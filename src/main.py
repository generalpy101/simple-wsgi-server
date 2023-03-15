import socket
import selectors
import types
from parsers.http_parser import parse_http

HOST = "0.0.0.0"
PORT = 5000

SERVER_CAPACITY = 1024
BUFFER_SIZE = 1024

default_selector = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addr = sock.accept()
    print(f"Accepted connection fron {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    default_selector.register(conn, events, data=data)


def service_connection(key: selectors.SelectorKey, mask: int):
    sock: socket.socket = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            default_selector.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(parse_http(data.outb.decode()))
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(SERVER_CAPACITY)
    print(f"Server listening on {HOST}:{PORT}")
    sock.setblocking(False)
    default_selector.register(sock, selectors.EVENT_READ, data=None)
    try:
        while True:
            events = default_selector.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    service_connection(key, mask)
    except KeyboardInterrupt:
        print("Keyboard interrupt, exiting")
    finally:
        default_selector.close()


if __name__ == "__main__":
    main()
