def count(word, letter):
    count =0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

word =input("Enter string : ")
letter = input("Enter letter to count: ")
count(word, letter)