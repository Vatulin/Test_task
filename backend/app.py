from http.server import HTTPServer, SimpleHTTPRequestHandler

if __name__ == '__main__':
    SimpleHTTPRequestHandler.do_GET = lambda self: (
        self.send_response(200),
        self.send_header('Content-type', 'text/plain'),
        self.end_headers(),
        self.wfile.write(b'Hello from Effective Mobile!')
    ) if self.path == '/' else SimpleHTTPRequestHandler.do_GET(self)
    
    with HTTPServer(('', 8080), SimpleHTTPRequestHandler) as server:
        server.serve_forever()