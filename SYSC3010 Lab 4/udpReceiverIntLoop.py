# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)
counter = 0

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    if (counter == 0):
        buf, address = s.recvfrom(port)
        n = (int)(buf)
        print ("Looping for " + (str)(buf)  + "loops")
    elif ((n + 1)  == (counter)):
        break
    else:
        buf, address = s.recvfrom(port)
        if not len(buf):
            break
        print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))

        #sending back new packet
        temp = buf.decode('utf-8');
        temp = "ACK: " + temp
        s.sendto(temp.encode('utf-8'), address)
    counter += 1
s.close()
