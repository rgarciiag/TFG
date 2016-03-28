#!/usr/bin/python

import socket

dest_addr = '192.168.1.1'
port = 53

icmp = socket.getprotobyname('icmp')
udp = socket.getprotobyname('udp')

recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)

recv_socket.settimeout(1)
send_socket.settimeout(1)

recv_socket.bind(("", port))
send_socket.sendto("", (dest_addr, port))

try:
    #_, curr_addr = recv_socket.recvfrom(512)
    #curr_addr = curr_addr[0]
    print str(recv_socket.recvfrom(512))
except socket.error:
    print "sdgsg"
    pass
finally:
    send_socket.close()
    recv_socket.close()

