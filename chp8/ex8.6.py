largest = None
smallest = None
testList = list()
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    
    testList.append(num)
print("Maximum is", max(testList))
print("Minimum is", min(testList))