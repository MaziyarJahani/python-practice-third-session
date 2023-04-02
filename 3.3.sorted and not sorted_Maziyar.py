list = input("please insert your list of numbers by using space between numbers:").split()
list = [int(num) for num in list]
a = 0
for i in range(len(list) - 1):
    if list[i] > list [i + 1]:
        a = a + 1
        break
if a == 0:
    print ("the list is sorted ✅")
else:
    print ("the list is not sorted ❌")