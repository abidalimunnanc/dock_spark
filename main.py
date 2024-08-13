import socket

def main():
    HOST = 'localhost'
    PORT = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on port {PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = input("Enter data to send: ")
                if not data:
                    break
                conn.sendall(data.encode())

if __name__ == "__main__":
    main()
