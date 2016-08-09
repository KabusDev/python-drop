import random

print ("dice thing, if you roll a double you score is set to 0") #intro
die1 = random.randrange(1,6)#die1 generator
die2 = random.randrange(1,6)#die2 generator
print ("1st Die:",die1,)
print ("2nd Die:",die2,)

score = die1 + die2
totalscore = score + die1 + die2
dies_equal = die1 == die2

if dies_equal: #if dies are equal, reset
    totalscore = 0
    print ("Equal Dice, You loose, Your score is: ",totalscore,)
    
else: #adding score
    score = die1 + die2
    print ("Your scored: ",score,)
    if score >0:
        print ("Total Score: ",totalscore,)

