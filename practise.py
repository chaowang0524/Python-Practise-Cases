import random
random.seed(50)
lst=[]

for i in range(30):
   lst.append(random.random())

print(lst[::-1])
