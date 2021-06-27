import socket
try:
    url = input("Enter URL: ")
    port = url.split("/")
    port = port[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((port, 80)) 
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode())
    mysock.close()
except:
    print("Error, enter a valid URL")