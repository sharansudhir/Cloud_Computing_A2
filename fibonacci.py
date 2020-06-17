import time
import csv
import matplotlib.pyplot as plt
values = []
times = []
def fib(n):
    lis = []
    f=0
    s=1

    if(n==0):
        lis.append(f)
    elif(n==1):
        lis.append(f)
        lis.append(s)
    else:
        lis.append(f)
        lis.append(s)
        for i in range(2, n):
            c = f + s
            f = s
            s = c
            lis.append(c)
  #  print(lis)
    return lis

f = open("random_numbers.txt")
line = f.read().splitlines()
line = [int(x) for x in line]


line = [int(x) for x in line]

final = []


for i in range(100):

    start = time.time()
    x=fib(line[i])
    end = time.time()
    values.append(line[i])
    times.append(end - start)

    res = [str(i+1),str(end - start),line[i],x]
    final.append(res)
   # print("Execution Time: " + str(end - start))

with open("fibonacci_log_file.csv","w+",newline="") as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(['Request ID','Execution Time','N','Result'])

    csvwriter.writerows(final)

plt.plot(values,times)
plt.xlabel("N Values ====>")
plt.ylabel("Execution Time ====>")
plt.title("Fibonacci Graph")
plt.show()