# x is a double digit number and it follows the rules below:
# 809*x =809*x+9*x
# 809*x is a 4 digit number
# 8*x is a double digit number
# 9*x is a three digit number
# find x 

# x is a double digit number:
for x in range(10,100):
    if 809 * x == 800 * x + 9 * x and 10000>809*x>999 and 100>8*x>9 and 1000>9*x>99:
        print(x,809*x)
