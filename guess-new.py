import random

highest = 10
answer = random.randint(1,highest)
print(answer)
guess = int(input("Guess a number between 1 and {}: ".format(highest)))

# if guess != answer:
#     if guess > answer:
#         print("guess less")
#     else:
#         print("guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("you did it")
#     else:
#         print("Sorry bro")
# else:
#     print("you did it 1st attempt")

if guess == answer:
    print("you did it at 1st attempt")
else:
    if guess > answer:
        print("guess lower")
    else:
        print("guess higher")
    guess = int(input())
    if guess == answer:
        print("you did it")
    else:
        print("sorry bro")
