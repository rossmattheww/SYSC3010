# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import random

host = sys.argv[1]
textport = sys.argv[2]
n = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
number = int(n) + 1
run = True
i = 0

while run:
    print ("Sending int")

#    s.sendall(data.encode('utf-8'))

    for i in range(0, number):
        if (i == 0):
            s.sendto(n.encode('utf-8'), server_address)
        else:
            data = random.randint(0,100)
            messLen = len((str)(data))
            if not len((str)(data)):
                break
            s.sendto(((str)(data)).encode('utf-8'), server_address)
            buf, address = s.recvfrom(port)
            print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))
        i+= 1
    run = False

s.close()

