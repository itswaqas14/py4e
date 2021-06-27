fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lines = []
for line in fh:
    lines = lines + line.split()

sort = []
for i in lines:
    if i not in sort:
        sort.append(i)
print(sorted(sort))