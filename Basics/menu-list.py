choice = "_"

while choice != "0":
    if choice in "12345":
        print("You have selected {}".format(choice))
        break
    else:
        print("please select an option")
        print("1.\t sleeping")
        print("2.\t eating")
        print("3.\t swimming")
        print("4.\t playing")
        print("5.\t coding")

    choice = input()
else:
    print("you selected 0. Game Over")
