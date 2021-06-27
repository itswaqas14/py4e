def computepay(h, r):
    if h>40:
        x = (h-40)*1.5 * r
        pay = 40 * r + x
    elif h<40:
        pay = h*r
    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)