from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl


class MyHttpServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.path = './index.html'
        elif self.path == '/page2':
            self.send_response(200)
            self.path = './pages/page2.html'
        else:
            self.send_response(404)
            self.path = './pages/404.html'
        return SimpleHTTPRequestHandler.do_GET(self)


my_object = MyHttpServer
port = 4443

httpd = HTTPServer(("", port), my_object)
httpd.socket = ssl.wrap_socket(
    httpd.socket, certfile="./SSL/certificate.pem", keyfile='./SSL/key.pem', server_side=True)
print("Servidor rodando na porta" + str(port))

httpd.serve_forever()
