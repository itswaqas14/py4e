import urllib.request, urllib.error, urllib.parse
try:
    url = input("Enter URL: ")
    fhand = urllib.request.urlopen(url)
    count =0
    doc = ''
    for line in fhand:
        doc = doc + line.decode()
        count = count + len(line)
    doc = doc[:3001]
    print(doc, end = '')
    print("Number of characaters is ",count)
except:
    print("Error, enter a valid URL")