import matplotlib.pyplot as plt
import numpy as np


input_file = open("out", "r")
#output_file = open("final", "w")
dates = []
threads = []

for line in input_file:
    split = line.split(' ')
    if len(split) > 1:
        if split[1] == "new_thread\n":
            if len(threads) == 0:
                threads.append(1)
                dates.append(split[0])
            else:
                threads.append(threads[len(threads)-1]+1)
                dates.append(split[0])
        if split[1] == "end_thread\n":
            threads.append(threads[len(threads) - 1] - 1)
            dates.append(split[0])
input_file.close()

'''
for i in threads:
    output_file.write("%s %s\n" % (dates[i], threads[i]))
output_file.close()
'''

plt.plot(threads)
plt.show()
