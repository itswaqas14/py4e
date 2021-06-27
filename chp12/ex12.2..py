import socket
try:
    url = input("Enter URL: ")
    count =0
    doc = ''
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
        count = count + len(data)
        doc = doc + str(data.decode())
    mysock.close()
    doc = doc[:3001]
    print(doc)
    print("Number of characaters is ",count)
except:
    print("Error, enter a valid URL")
