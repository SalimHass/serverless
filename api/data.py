from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    s=self.path
    url_components= parse.urlsplit(s)
    query_string_list=parse.parse_qsl(url_components.query)
    dic= dict(query_string_list)
    name= dic.get("name")

    if name:
        message= f"hi {name}"
    else:
        message= "hi stranger"
    
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    self.wfile.write(("the time is "+ str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))).encode()
    return
