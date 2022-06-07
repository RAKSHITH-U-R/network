import http.server
import socketserver
from urllib.parse import unquote

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = '\n'.join([unquote(x) for x in self.rfile.read(length).decode().split('&')[:-1]]) + '\n\n\n\n'
        with open('registrations.txt', 'a+') as f:
            f.write(data)
            
        #redirect to homepage
        self.send_response(303)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Location', '/')
        self.end_headers()
        return
    
handler_object = MyHttpRequestHandler
my_server = socketserver.TCPServer(('localhost',8000), handler_object)
my_server.serve_forever()
