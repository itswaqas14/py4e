import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

uh = urllib.request.urlopen(url, context=ctx).read()
data = uh.decode()
#print(len(data))
count =0
js = json.loads(data)


for item in js['comments']:
    #print(item['count'])
    num = int(item['count'])
    count = num + count
print(count)