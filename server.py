import argparse
import socket


def run_server(ip, port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    conn, addr = server.accept()
    with conn:
        print(f"connection by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received message:", data.decode("utf-8"))


def get_args():
    parser = argparse.ArgumentParser(description="Recieve data from client")
    parser.add_argument("port", type=int, help="the server's port")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    run_server("127.0.0.1", args.port)
