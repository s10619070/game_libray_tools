# Dice Rolling Library, Zacari Brady, feburary 18, 2021, 1:44

import random

# d4 Simulator
def roll_d4(num_roll): # num_roll is an ARGUMENT
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 4)
        print(f"You have rolled a {results}./n")
        time.sleep(1)
        rolls += 1 # Increments rolls by 1 each time. 
        the_sum += result
    print(f"The total of the {num_roll} rolls was {the_sum}\n") # use this line to print the sum.

roll_d4(5) # This will roll the d4 FIVE times.
   # roll_d4(4) No longer needed after testing.
    
   # d6

   # d8

   # d10

   # d12

   # d20

   # d100