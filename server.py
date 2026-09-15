import argparse
import socket
from threading import Thread


def run_server(ip, port):

    # listen for connection, and then infinitly create threads for any connection made

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        t = Thread(target=handle_connection, args=(conn, addr))
        t.run()


def handle_connection(conn, addr):

    # open connection to conn, and receive data and data length
    with conn:
        print(f"connection by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received message:", data.decode("utf-8"), data)


def get_args():
    parser = argparse.ArgumentParser(description="Recieve data from client")
    parser.add_argument("ip", type=str, help="the server's ip")
    parser.add_argument("port", type=int, help="the server's port")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    run_server(args.ip, args.port)
