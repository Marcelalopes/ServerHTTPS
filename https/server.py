from cgitb import html
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

# classe que recebe o método "SimpleHTTPRequestHandler" faz o mapeamento dos diretórios que serão utilizados
# pelo servidor http


class MyHttpServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = './pages/index.html'
        elif self.path == '/page2':
            self.path = './pages/page2.html'
        else:
            self.path = './pages/404.html'
        return SimpleHTTPRequestHandler.do_GET(self)


# Variavel que recebe o objeto do servidor http
my_object = MyHttpServer

# definindo a porta que será utilizada
port = 8080
# inicia o servidor http passando o ip, porta, e o objeto com os diretórios
httpd = HTTPServer(("localhost", port), my_object)

# Faz a autenticação utilizando os certificado autoassinados e chave criados no open ssl
httpd.socket = ssl.wrap_socket(
    httpd.socket, certfile="./SSL/certificate.pem", keyfile='./SSL/key.pem', server_side=True)

print("Servidor rodando na porta: " + str(port))

# método para processar uma ou várias requisições.
httpd.serve_forever()
