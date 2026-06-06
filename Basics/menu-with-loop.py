available_parts = ["keyboard", "mouse", "monitor", "cpu", "mouse pad"]
choice = "_"
computer_parts = []
while choice != "0":
    if choice in "12345":
        print("selected {}".format(choice))
        computer_parts.append(choice)
    else:
        print("select any option")
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1, part))
    choice = input()
print(computer_parts)
