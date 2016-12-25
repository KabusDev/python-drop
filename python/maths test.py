import random
import time

qnum=1
quizscore = 0
yes = set(['yes','y', 'ye',])
no = set(['no','n'])

user = input("Please Enter your name: ").title() #.title makes input first letter capitalised
uclass = input("Please Enter your class: ").upper()
print ("Hello", user)
print ("Your class is ", uclass)
print ("Welcome to the Maths Quiz, there will be 10 questions")

while qnum < 11:
    print("Question", qnum)
    
    #random.randint need to be in while loop as if not they repeat same number generated
    mrandom1 = random.randint(1,10)
    mrandom2 = random.randint(1,10)  #so it doesnt divide by 0, 1 is initial number, else i would use randrange(10)
    multiply = mrandom1 * mrandom2
    subtract = mrandom1 - mrandom2
    addition = mrandom1 + mrandom2 #set all maths commands here
    test = random.randint(1,3)

    if test ==(1):
        print (mrandom1, "+", mrandom2)
        answer = addition
    elif test ==(2):
        print (mrandom1, "x", mrandom2)
        answer = multiply
    else:
        test ==(3)
        print (mrandom1, "-", mrandom2)
        answer = subtract

    while True:
      try:
        uanswer = int(input())  #accepts only intergers
      except ValueError:
        print ("That is not a valid answer")
        continue #stops errors from being printed and continues uanswer
      else:
        break

    if uanswer == answer:
        print("Correct")
        quizscore += 1
    else:
        print("Incorrect, The answer was:", answer) #issue, answer is rounded to 1sf, logic error somewhere, (seems to be fixed?)
    qnum += 1

print("Well done", user, "you scored", quizscore, "/10")

#saving stuff

savedata = open('test_results.txt','a')
data = user, uclass, quizscore #string needed
print ("Saving your work.")
savedata.write(str(data))#prints created string of user inputted variables
savedata.write("pls work")
savedata.write('\n')#writes new line for rerunning py file to write new scores
print("Thank you for completing your quiz")
time.sleep(5)
exit()
