import random
import sys
random_list = []
z = 0
n = int(input("please enter your number:"))
#random_list = random.sample(range(-sys.maxsize, sys.maxsize),n)
#print(random_list)
while z < n:
    y = random.randint(-sys.maxsize , sys.maxsize)
    if y in random_list:
        z = z + 0
    else:
        random_list.append(y)
        z = z + 1
else:
    print (random_list)