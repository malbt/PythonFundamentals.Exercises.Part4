from random import randint

number = randint(1,10)
guess = int(input("guess a number between 1 and 10"))

while guess != number:
    if guess<number:
        print (number)
        print(guess)
        print("Too low!")
        guess = int(input("guess a number between 1 and 10"))

    elif guess > number:
        print(number)
        print(guess)
        print("Too high!")
        guess = int(input("guess a number between 1 and 10"))

print("you guessed right")
