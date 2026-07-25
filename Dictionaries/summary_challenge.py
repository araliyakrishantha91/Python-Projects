choice = "_"
while choice != "0":
    #if choice in list("12345"):
    #if choice in set("12345"):
    if choice in {"1","2","3","4","5"}:
        print(f"You chose {choice}")
    else:
        print("Please choose your option from the list below")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tLearn swimming")
        print("4:\tHave dinner")
        print("5:\tgo to bed")
        print("0:\tExit")
    choice = input()
