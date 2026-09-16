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
        t.start()


def handle_connection(conn, addr):

    # open connection to conn, and receive data and data length
    with conn:
        print(f"connection by {addr}")

        while True:
            data_len = conn.recv(4)
            data_len = int.from_bytes(data_len, byteorder="little")
            data = conn.recv(data_len)
            while len(data) < data_len:
                data += conn.recv(data_len - len(data))
            if not data:
                break
            print("Received message:", data_len, data.decode("utf-8"))


def get_args():
    parser = argparse.ArgumentParser(description="Recieve data from client")
    parser.add_argument("ip", type=str, help="the server's ip")
    parser.add_argument("port", type=int, help="the server's port")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    run_server(args.ip, args.port)
