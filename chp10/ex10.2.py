name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)
hours = dict()
for line in fhandle:
    if line.startswith("From "):
        line = line.split()
        time = line[5]
        hour = time[0:2]
        hours[hour] = hours.get(hour, 0) +1

hourList = []
for hour, count in hours.items():
    hourList.append((hour, count))
hourList.sort()
for hour, count in  hourList:
    print (hour, count)