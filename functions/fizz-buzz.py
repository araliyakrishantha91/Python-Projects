def fizz_buzz(number: int) -> str:
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

input("Play fizz buzz game! press Enter")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your turn: ")
    if correct_answer != player_answer:
        print("You loss! the correct answer is {}".format(correct_answer))
        break
else:
    print("Well done. you have reached {}".format(next_number))
