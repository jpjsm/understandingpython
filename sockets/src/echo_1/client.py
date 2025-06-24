"""echo client."""

import socket

SERVER = "127.0.0.2"  # The server's hostname or IP address
LISTENING_AT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER, LISTENING_AT))
    for i in range(10):
        msg = f"Hello, world... for the {i+1} time."
        s.sendall(bytes(msg, encoding="utf-8"))
        data = s.recv(1024)
        print(f"Received {data!r}")

print("Done !!")
