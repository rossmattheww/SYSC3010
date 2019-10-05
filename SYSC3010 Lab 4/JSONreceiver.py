import json
import socket, sys, time

textport = sys.argv[1]


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

for i in range(0,10):
    buf, address = s.recvfrom(port)
    if not len(buf):
        break
    x = json.loads(buf.decode('utf-8'))
    print(x)

