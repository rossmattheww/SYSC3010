import json
import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

x = '{"name":"John","age":30,"city":"New York"}'
y = json.loads(x)
i = 0
for i in range(0,10):
    data = json.dumps(y).strip()
    #update y
    y["age"] = y["age"] + 1
    s.sendto(data.encode('utf-8'), server_address) #send y
    print(data)

