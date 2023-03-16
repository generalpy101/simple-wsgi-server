import socket
import selectors
import types
from parsers.http_parser import parse_http
from models.http_request import HTTPRequest

HOST = "0.0.0.0"
PORT = 5000

SERVER_CAPACITY = 1024
BUFFER_SIZE = 1024

default_selector = selectors.DefaultSelector()


def view(environ):
    path = environ.get("PATH_INFO")
    return f"Hello from {path}\n"


def application(environ, start_response):
    response = view(environ)
    start_response("200 OK", [("Content-Length", len(response))])
    return [response]


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
            data.inb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            default_selector.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.inb:
            print(data.inb.decode())
            request = HTTPRequest(**parse_http(data.inb.decode()))

            def start_response(status, headers):
                sock.sendall(f"{request.protocol} {status}\r\n".encode())
                for key, value in headers:
                    sock.sendall(f"{key}: {value}\r\n".encode())
                sock.sendall("\r\n".encode())

            environ = request.to_environ()
            response = application(environ, start_response)
            for content in response:
                sock.sendall(content.encode("utf-8"))
            data.inb = ""


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
    except Exception as exception:  # pylint: disable=broad-exception-caught
        print(exception)
    finally:
        print("Closing server, bye!")
        sock.close()
        default_selector.close()


if __name__ == "__main__":
    main()
