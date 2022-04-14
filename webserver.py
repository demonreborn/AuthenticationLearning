from http.client import HTTPS_PORT
import http.server
import cgi
import socketserver

form = cgi.FieldStorage()

index_path = "index.html"

class webHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        print("POST received")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("This was a successful post.".encode('utf-8'))

    def do_GET(self): # do_GET request handlet (Get requests)
        print("GET received")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        # self.end_headers()
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8000
Handler = webHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
