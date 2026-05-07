answer = 5
print("guess a number :")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done. you guessed it")
    else:
        print("Sorry you haven't guessed correctly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done. you guessed it")
    else:
        print("Sorry you haven't guessed correctly")
else:
    print("You got it first time")
