available_parts = ["keyboard", "mouse", "monitor", "cpu", "mouse pad", "router"]
choice = "_"
computer_parts = []
while choice != "0":
    if choice in "123456":
        print("selected {}".format(choice))
        if choice == "1":
            computer_parts.append("keyboard")
        elif choice == "2":
            computer_parts.append("mouse")
        elif choice == "3":
            computer_parts.append("monitor")
        elif choice == "4":
            computer_parts.append("cpu")
        elif choice == "5":
            computer_parts.append("mouse pad")
        elif choice == "6":
            computer_parts.append("router")
    else:
        print("select any option")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
    choice = input()
print(computer_parts)
