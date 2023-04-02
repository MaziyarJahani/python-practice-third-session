a = int(input("please enter first positive number:"))
b = int(input("please enter second positive number:"))
LCM = 0
for i in range(1, a*b + 1):
    if i % a == 0 and i % b == 0:
        LCM = i
        break
print(LCM)