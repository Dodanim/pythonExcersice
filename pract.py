from random import randint

#generate a random number from 1 to 7
lucky_number = randint(1,7)

#ask the user to guess a number from 1 to 7
user_guess = int(input('Guess a number from 1 to 7: '))

#determine if the user has guessed correctly
if user_guess ==lucky_number:
    print("you guessd correctly!")
else:
    print("Print guessed incorrectly")
    print("The lucky number was: ", lucky_number)