name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        email = line[1]
        pos = email.index("@")
        domain = email[pos+1:]
        emails[domain] = emails.get(domain, 0) +1

print(emails)