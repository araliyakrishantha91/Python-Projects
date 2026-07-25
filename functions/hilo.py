LOW  = 1
HIGH = 1000
# print("Think a number between {} and {}".format(low , high))
# answer = int(input("Enter the answer "))

def guess_binary(answer, low, high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses
        # print("{}".format(guess))
        guesses += 1

correct_count = 0
max_guesses = 0

for number in range(LOW, HIGH+1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {} guesses".format(number,number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("{} is the max guesses and happened {} times".format(max_guesses, correct_count))
