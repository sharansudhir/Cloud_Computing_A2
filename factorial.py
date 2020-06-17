import timeit
import matplotlib.pyplot as plt
import time
import csv
values = []
times = []
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
   # print(fact)
    return fact

f = open("random_numbers.txt")
line = f.read().splitlines()
line = [int(x) for x in line]

final = []

for i in range(100):
 #   start = timeit.default_timer()
    start  = time.time()
    x=fact(line[i])
    end = time.time()
  #  end = timeit.default_timer()
    values.append(line[i])
    times.append(end-start)
#    print("Execution Time: "+str(end-start))
    res = [str(i+1),str(end - start),line[i],x]
    final.append(res)

with open("factorial_log_file.csv", "w+", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(['Request ID', 'Execution Time', 'N', 'Result'])

    csvwriter.writerows(final)
plt.plot(values,times)
plt.xlabel("N Values ====>")
plt.ylabel("Execution Time ====>")
plt.title("Factorial Graph")
plt.show()

