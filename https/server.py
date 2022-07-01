from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
class MyHttpServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = './pages/index.html'
        elif self.path == '/page2':
            self.path = './pages/page2.html'
        return SimpleHTTPRequestHandler.do_GET(self)

my_object = MyHttpServer
port = 4443
httpd = HTTPServer(("", port), my_object)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile="./SSL/certificate.pem", keyfile='./SSL/key.pem', server_side=True)

print("Server running on https://localhost:" + str(port))

httpd.serve_forever()