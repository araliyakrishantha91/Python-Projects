import random

highest = 1000
answer = random.randint(1,highest)
print(answer)
guess = None

while guess != answer:
    guess = int(input("guess a number between 1 and {}: ".format(highest)))
    if guess == 0:
        print("Game Over")
        break
    if guess == answer:
        print("you guessed correctly")
        break
    else:
        if guess > answer:
            print("guess lower")
        else:
            print("guess higher")
