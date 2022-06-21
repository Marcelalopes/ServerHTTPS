from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

port = 4443
httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile="./SSL/certificate.pem", keyfile='./SSL/key.pem', server_side=True)

print("Server running on https://localhost:" + str(port))

httpd.serve_forever()