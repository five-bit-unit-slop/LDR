import socket

HOST = "0.0.0.0"
PORT = 8080
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"UDP server listening on port {PORT}")

try:
    while True:
        data, address = server.recvfrom(BUFFER_SIZE)

        print(f"\nRequest from {address}:")
        print(data.decode("utf-8", errors="replace"))

        server.sendto(b'{"status":"received"}', address)

except KeyboardInterrupt:
    print("\nShutting down...")
finally:
    server.close()
