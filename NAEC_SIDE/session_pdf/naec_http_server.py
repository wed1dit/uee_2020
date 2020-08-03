import http.server
import socketserver

# TODO securtiy level = -1242141 :(

Handler = http.server.SimpleHTTPRequestHandler
host = 'localhost'
PORT = 55001
with socketserver.TCPServer((host, PORT), Handler) as httpd:
    print(f'server is running at {host}:{PORT}')
    httpd.serve_forever()