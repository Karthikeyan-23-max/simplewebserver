# EX01 Developing a Simple Webserver
## Date:
27/03/2025
## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.


## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```

## OUTPUT:

![output](<Screenshot 2025-03-27 110257.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
