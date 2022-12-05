import time

# time.time() # the float number of seconds since the Unix epoch

# convert it to readable time format

# print(time.ctime(time.time())) # Mon Dec  5 02:18:09 2022
# print(time.asctime()) # Mon Dec  5 02:18:28 2022
# print(time.ctime()) # Mon Dec  5 02:19:26 2022

start = time.time() # get the current time (in float for calculation)

# the program starts
for i in range(10000):
    print(i)
# the program ends
end = time.time()

# get the running time

print(end-start)
