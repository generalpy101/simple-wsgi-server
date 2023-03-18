import socket
from multiprocessing.pool import ThreadPool

from libs.logger import get_logger
from parsers.http_parser import parse_http
from models.http_request import HTTPRequest

logger = get_logger(__name__)

BUFFER_SIZE = 1024


def view(environ):
    path = environ.get("PATH_INFO")
    return f"Hello from {path}\n"


def application(environ, start_response, request):
    response = view(environ)
    start_response("200 OK", [("Content-Length", len(response))], request)
    return [response]


class ThreadedServer:
    def __init__(self, host, port, buffer_size=BUFFER_SIZE, num_workers=1024) -> None:
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.workers = num_workers
        self.thread_pool = ThreadPool(processes=num_workers)

    def listen(self):
        try:
            self.socket_server.bind((self.host, self.port))
            self.socket_server.listen(self.workers)
            logger.info(f"Server listening on {self.host}:{self.port}")
            while True:
                conn, addr = self.socket_server.accept()
                self.thread_pool.map_async(self._service_connection, [conn])
                print(f"Accepted connection from {addr}")
        except OSError as exception:
            logger.error(exception)
        except Exception as exc:
            logger.error(exc)
        finally:
            self.socket_server.close()

    def _service_connection(self, connection: socket.socket):
        is_there_data = False
        final_request = ""

        def start_response(status, headers, request):
            connection.sendall(f"{request.protocol} {status}\r\n".encode())
            for key, value in headers:
                connection.sendall(f"{key}: {value}\r\n".encode())
            connection.sendall("\r\n".encode())

        print("Servicing socket")
        while True:
            recv_data = connection.recv(self.buffer_size)
            if recv_data:
                parsed_request = parse_http(recv_data.decode())
                http_request = HTTPRequest(**parsed_request)
                # print(http_request.to_environ())
                print(http_request.to_string())
                environ = http_request.to_environ()
                response = application(environ, start_response, http_request)
                for content in response:
                    connection.sendall(content.encode("utf-8"))
                self._close_connection(connection)
                return
            else:
                self._close_connection(connection)
                return

    def _close_connection(self, connection: socket.socket):
        logger.info("Closing connection")
        connection.close()

    def __del__(self):
        self.thread_pool.terminate()
        self.socket_server.close()
