count =0
total =0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    count = count +1
    total = num +total
    average = total /count

print(total, count, average)