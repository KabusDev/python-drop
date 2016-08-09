import random


print ("dice thing, if you roll a double you score is set to 0") #intro
die1 = random.randrange(1,6)#die1 generator
print die1
die2 = random.randrange(1,6)#die2 generator
print die2
if die1 == die2: #if dies are equal, reset
    score = 0
    print ("Your score is: ",score,)
else:
    score = die1 + die2
    print ("Your score is: ",score,)
