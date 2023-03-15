import socket
import sys
from parsers.http_parser import http_parser

HOST = "0.0.0.0"
PORT = 5000

SERVER_CAPACITY = 1024
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(SERVER_CAPACITY)
        print(f"Server listening on {HOST}:{PORT}")
        conn, addr = sock.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                print(data.decode())
                conn.sendall(data)


if __name__ == "__main__":
    main()
