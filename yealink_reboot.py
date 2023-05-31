#!/usr/bin/env python

# Reboot Yealink phones by sending HTTP GET request like this:
# http://login:password@ip_address/servlet?key=Reboot

import socket, base64

phones = {
'a1.b1.c1.d1':'user1:password1',
'a2.b2.c2.d2':'user2:password2',
'an.bn.cn.dn':'user3:password3'
}

for ip in phones:
  try:
    credentials_bytes = phones[ip].encode('ascii')
    base64_bytes = base64.b64encode(credentials_bytes)
    credentials_base64 = base64_bytes.decode('ascii')
    request = 'GET /servlet?key=Reboot HTTP/1.1\r\nHost: '+ip+'\r\nAuthorization: Basic '+credentials_base64+'\r\n\r\n'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 80))
    s.send(request.encode())
    result = s.recv(1024)
    s.close()
  except:
    pass
