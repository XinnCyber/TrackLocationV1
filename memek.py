#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("[*] Masukan Host Untuk Scanning: ")

def portscanner(port):
        if sock.connect_ex((host,port)):
                print(colored("[!!] Port %d Kaga Bisa Coy" % (port), 'blue'))
        else:
                print(colored("[!!] Port %d Bisa Ngab" % (port), 'green'))
                
for port in range(1,1000):
        portscanner(port)
