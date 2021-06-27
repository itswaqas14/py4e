name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)
emails = dict()
for line in fhandle:
    if line.startswith("From "):
        line =line.split()
        email = line[1]
        emails[email] = emails.get(email, 0) +1

emailList = []
for emails, count in emails.items():
    emailList.append((count, emails))
emailList.sort(reverse = True)

print(max(emailList))
