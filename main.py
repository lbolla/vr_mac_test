import sys
import uuid
import http.server
import socketserver

PORT = int(sys.argv[1])

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        body = '''
        MAC={}
        UUID1={}
        UUID4={}
        '''.format(
            hex(uuid.getnode()),
            uuid.uuid1(),
            uuid.uuid4(),
        )
        self.wfile.write(body.encode())

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
