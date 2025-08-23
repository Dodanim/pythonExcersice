from random import randint
"""The Magic 8 Ball is a plastic sphere, made to look like an oversized eight ball, which is used for fortune-telling or seeking advice.’ It was invented in 1946 by Albert C. Carter and Abe Bookman (Reference: Wikipedia). 
Your task is to create a Python script (magic8Ball.py) that meets the following project requirements.
•	The user should be presented with a welcome message.
•	The user should be asked to enter a question and to press the ENTER key.
•	The script should then display the word ‘shaking’ 4 times.
•	A random number should be generated from 1 to 8 (inclusive).
•	The script should determine which random number was generated and display an appropriate message (see the table below).
•	The message should be displayed in the console.
"""
def showAnswer(randomNumber):
    answerBall=("It is certain", "As I see it, yes", "Reply hazy, try agian", "Do not count on it","It is decidedly so", "Most likely", "Ask me again later", "My sources say no")
    print(answerBall[randomNumber])
     

print("Welcome to Magic 8 Ball!!")
question = input("Ask your question and press ENTER: ")
i = 1
while i<5:
    print("Shaking...")
    i+=1
randomNumber = randint(1,8)
showAnswer(randomNumber)
