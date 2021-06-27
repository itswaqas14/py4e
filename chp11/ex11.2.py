import re

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)
sum = 0
count = 0

for line in fhandle:
    line = line.rstrip()
    num = re.findall('New Revision: ([0-9]+)', line)
    for n in num:
        n = float(n)
        sum = sum + n
        count += 1

avg = sum / count
print(int(avg))