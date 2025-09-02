from random import randint

numberUser = int(input("Guess the magic number between 1 to 10: "))
numberMachine = randint(1,10)
if(numberUser == numberMachine):
    print("You won!")
else :
    print("You lose!")