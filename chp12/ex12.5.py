import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
doc = ""
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    doc = doc + data.decode()
mysock.close()
pos = doc.find("\r\n\r\n")
doc = doc[pos+4:]
print(doc)