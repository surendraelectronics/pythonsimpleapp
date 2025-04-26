import http.server
import socketserver

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # Send message
            message = "Hello from Python Server!"
            self.wfile.write(message.encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('404 Not Found'.encode())

# Set port number
PORT = 8000

# Create server
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print(f"Try accessing http://localhost:{PORT}/hello")
    # Start server
    httpd.serve_forever()
