import random

mylist = []

for i in range(100):
    x = random.randint(1,100)
    mylist.append(x)

mylist.sort()
f = open('random_numbers.txt',"w+")

for i in range(100):
    f.write(str(mylist[i])+"\n")
