a = int(input("please enter first positive number:"))
b = int(input("please enter second positive number:"))
GCD = 1
if a >= b:
    for i in range(1, b+1):
        if a % i == 0 and b % i == 0:
            GCD = i
else:
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            GCD = i
print(GCD)