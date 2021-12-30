import os
from http.server import HTTPServer, BaseHTTPRequestHandler



class Serv(BaseHTTPRequestHandler):

    protocol_version = "HTTP/1.1"

    def result(self):
        try:
            content = self.path.split('/')
            b, a = int(content[-1]), int(content[-2])
            if (content[-3] == 'add'):
                c = a + b
            elif (content[-3] == 'multiply'):
                c = a * b
            elif (content[-3] == 'substract'):
                c = a - b
            elif (content[-3] == 'divide'):
                if (b == 0):
                    c = "Error 422 : Can't divide by 0!! :O"
                else:
                    c = a / b
            else:
                c = "Error 422 : Invalid operator"
            resp = str(c)
            return resp
        except ValueError:
            return "Error 400 : Impossible request"

    def do_GET(self):
        
        resp = self.result()
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(resp.encode())  
        self.send_header('Content-length', f'{len(resp)}')

def main():
    port = 3000
    server_object = HTTPServer(('', port), Serv)
    server_object.serve_forever()
    

if __name__ == "__main__":
    main()


