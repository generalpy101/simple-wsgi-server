from server import ThreadedServer

HOST = "0.0.0.0"
PORT = 5000

SERVER_CAPACITY = 1024
BUFFER_SIZE = 1024

if __name__ == "__main__":
    # main()
    serv = ThreadedServer(HOST, PORT)
    serv.listen()
