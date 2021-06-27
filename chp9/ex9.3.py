name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        email = line[1]
        emails[email] = emails.get(email, 0) +1
print(emails)