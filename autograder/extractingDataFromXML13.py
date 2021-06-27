import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"

xml = urllib.request.urlopen(url, context=ctx).read()
print(xml.decode())

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print("Count: " + str(len(counts)))

sum = 0

for count in counts:
    sum += int(count.text)

print("Sum:" + str(sum))