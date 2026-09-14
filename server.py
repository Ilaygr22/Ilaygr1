import socket


def run_server (ip, port):
    
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

run_server('127.0.0.1', 65432)
