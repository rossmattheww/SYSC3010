# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
n = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
number = int(n)

while 1:
    print ("Enter data to transmit: ENTER to quit")
    data = sys.stdin.readline().strip()
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    i = 0
    for i in range(0,10):
        sendNew = data + "i"
        s.sendto(sendNew.encode('utf-8'), server_address)
        print "test1"
        buf, address = s.recvfrom(port)
        print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))
        i += 1
        
s.shutdown(1)

