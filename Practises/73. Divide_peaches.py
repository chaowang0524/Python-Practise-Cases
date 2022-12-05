# There were some peaches and five monkeys on the beach. The first monkey divided the peaches into 5 portions and there was one peach left. 
# The monkey threw the left one away and took one portion.
# The second monkey divided the peaches into 5 portions and there was one peach left too. He threw it way and took one portion.
# So did the third, the fourth and the last monkey.
# How many peaches at least were there on the beach at the first place?

# enumeration all possible answers and check one by one



# enumerate from 0 
x = 5 
while True:
    #check x 
    def check(x:int) ->bool:
        """check if the number is the answer

        Args:
            x (int): the number of the peaches

        Returns:
            bool: True or False
        """
        # There is always one peach left after the division:
        # if x is not the answer, return False
        for i in range(5):
            if x % 5 != 1:
                return False
            else:
                # if x goes through, keep rolling until it matches the final answer
                x = (x-1)/5*4
        return True

    # if x is the answer
    if check(x) == True:
        print(f"The answer is {x}")
        break
    else:
    # check next number
        x += 1