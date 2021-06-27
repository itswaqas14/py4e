# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
fh = open(fname)
avg = 0
count =0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(':')
    sliced = line[pos+1:]
    sliced = sliced.lstrip()
    num = float(sliced)
    avg = avg + num
    count = count +1
    
print("Average spam confidence:",avg/count)