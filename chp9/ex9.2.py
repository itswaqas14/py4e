name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        day = line[2]
        emails[day] = emails.get(day, 0) +1
print(emails)