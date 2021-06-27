import re
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)
regex = input("Enter a regular expression: ")
count =0
for line in fhandle:
    line = line.rstrip()
    x = re.findall(regex, line)
    if len(x) == 0:
        continue
    else:
        count = count +1
print("mbox.txt had", count, "lines that matched", regex)