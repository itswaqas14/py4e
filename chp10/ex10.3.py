import string
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)
letters = dict()
for line in fhandle:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    line = line.split()
    for word in line:
        word = list(word)
        for letter in word:
            letters[letter] = letters.get(letter, 0)+1

letterList =[]
for letter, count in letters.items():
    letterList.append((count, letter))
letterList.sort(reverse = True)

for count, letter in letterList:
    print(letter, count)