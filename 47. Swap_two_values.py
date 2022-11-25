a = 10
b = 20
# introducing third party variable

# c = a # save a to the third party variable (so a becomes empty or available to use )
# a = b # put the value of b to a (then b becomes empty or available to use)
# b = c # put c back to b so the swap is achieved

# operation

a = a+b # get the sum (c) of the two values
b = a-b # subtract b from the sum (c), leaves a and assign it to b 
a = a-b # subtract the new b (the swapped b) from the sum (c), leaves a and assign it to a so swap is achieved