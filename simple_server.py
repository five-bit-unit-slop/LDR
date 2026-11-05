from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):

    def handle_request(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length else b""

        print(f"\n[{self.command}] {self.path}")
        print("Headers:", self.headers)
        print("Body:", body.decode("utf-8", errors="replace"))

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status":"received"}')

    do_GET = handle_request
    do_POST = handle_request
    do_PUT = handle_request
    do_PATCH = handle_request
    do_DELETE = handle_request

server = HTTPServer(("0.0.0.0", 8080), RequestHandler)

print("Server listening on http://0.0.0.0:8080")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down...")
    server.server_close()