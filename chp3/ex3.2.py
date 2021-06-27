try:
    hrs = input("Enter Hours: ")
    h = float(hrs)
    rate = input("Enter rate: ")
    r = float(rate)
except:
    print("Error, please enter numeric input")
    exit()
x=0
if h>40:
    x = (h-40) *1.5*r
    h = 40
pay = (r*h) + x
print(pay)