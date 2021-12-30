import os
import requests
import ssl
import json
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler



class Serv(BaseHTTPRequestHandler):

    protocol_version = "HTTP/1.1"

    def result(self, a, b, operation):

        if (operation == 'add'):
            c = a + b
        elif (operation == 'multiply'):
            c = a * b
        elif (operation == 'substract'):
            c = a - b
        elif (operation == 'divide'):
            if (b == 0):
                c = "422 : Can't divide by 0!! :O"
            else:
                c = a / b
        else:
            c = "422 : Invalid Operation"
        return c

    def do_GET(self):
        resp = ""

        try:
            content = self.path.split('/')
            b, a = int(content[-1]), int(content[-2])
            operation = content[-3]
        except ValueError:
            resp = "400 : Impossible Request"

        if (resp == ""):
            resp = self.result(a, b, operation)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        if (str(resp) == resp):
            self.wfile.write(json.dumps({'Error': resp}).encode())
        else:
            self.wfile.write(json.dumps({'result': resp}).encode())

    def do_POST(self):
        ctype = self.headers['Content-Type']
        clen = int(self.headers['Content-Length'])
        r = json.loads(self.rfile.read(clen))
        resp = ""
        
        for key in r:
            if (key == "operation"):
                operation = r[key]
            elif (key == "arguments"):
                [a, b] = r[key]
            else:
                resp = "400 : Impossible Request"

        if (resp == ""):
            resp = self.result(a, b, operation)

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # send the message back
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        if (type(resp) == int) or (type(resp) == float) :
            output = '{ "result" : ' + str(resp) + ' }'
        else :
            output = '{ Error ' + resp + ' }'
        
        self.wfile.write(output.encode())
        self.send_header('Content-length', f'{len(output)}')


def main():
    port = 443
    server_object = HTTPServer(('', port), Serv)
    server_object.socket = ssl.wrap_socket (server_object.socket, server_side=True, certfile="cert.pem", keyfile="key.pem", ssl_version=ssl.PROTOCOL_TLSv1_2)
    server_object.serve_forever()

if __name__ == "__main__":
    main()
