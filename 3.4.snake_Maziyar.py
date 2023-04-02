n = int(input("please enter your number:"))
list1 = ["#*"]
list2 = ["*"]
while n > 0:
    if n % 2 == 0:
        print(list1[0] , end="")
        n = n - 2
    elif n % 2 == 1:
        print(list2[0] , end="")
        n = n -1