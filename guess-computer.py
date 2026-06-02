low  = 1
high = 1000
guesses = 1
print("Think a number between {} and {}".format(low , high))
input("press Enter to start the game")

while low != high:
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. Tell me should I guess higher(h), lower(l) or c if correct, o for exit: ".format(guess)).casefold()

    if high_low == "h":
        #guess higher. low of the range is 1 greater than guess
        low = guess + 1
    elif high_low == "l":
        #guess lower. high of the range is 1 lower than guess
        high = guess - 1
    elif high_low == "c":
        print("Well done, you guessed correctly by {} guesses".format(guesses))
        break
    elif high_low == "o":
        print("Game Over")
        break
    else:
        print("enter h,l or c")
    guesses += 1

else:
    print("I guessed number {}".format(low))
    print("I guessed it by {} guesses".format(guesses))
