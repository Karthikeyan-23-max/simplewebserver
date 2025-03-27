from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
    <head>
        <title>
            TCP/IP
        </title>
    </head>
    <body bgcolor="white">
       <center> <font color="Blue" size="100" >TCP/IP PROTOCALS<br></font></center>
        <h2>1.Application Layer HTTP, FTP, SSH, TELNET & DNS. </h2>

        <h2> 2.Transport Layer TCP, UDP.</h2>
            
        <h2>3.Internet Layer ICMP, IGMP, ARP, IPv4/IPv6. </h2>

        <h2>4.Network Access Layer Ethernet, FDDI, X.25, Frame Relay , Token Ring. </h2>
        
    
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()