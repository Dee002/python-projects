import random 

number = random.randrange(0,20)
guess = int(input("Guess a number between 0 and 50: "))

while guess != number:
    if guess < number:
        print("You need to guess higher")
        guess = int(input("Guess a number between 0 and 50: "))
    else:
        print("You need to gues lover")
        guess = int(input("Guess a number between 0 and 50: "))
        
print("Congrats you won!!")