# app.py 
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT=8000

class MyHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    sef.send_header('Content-type','text/html')
    self.end_header()
    self.wfile.write(b'Hell0,World!This is my Python web application.')

httpd = HTTPServer((",PORT).MyHandler)
print(f'Serving on port{",PORT}...')
httpd.serve_forever()
