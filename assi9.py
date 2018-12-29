#qu n0-9 by susmita rudra pal
n = int(input("Enter a Number :"))

rev = 0
fd = 0
s = 0

ld = n % 10

while n > 0:
    r = n % 10

    rev = rev * 10 + r

    n = int(n / 10)

fd = rev % 10

s = fd + ld

print("Sum of first and last digit is :", s)
