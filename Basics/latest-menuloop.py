available_parts = ["keyboard", "mouse", "monitor", "cpu", "router" , "speaker"]
available_choices = [str(i) for i in range(1, len(available_parts) + 1)]
print(available_choices)
choice = "_"
computer_parts = []
while choice != "0":
    if choice in available_choices:
        index = int(choice) - 1
        choose_part = available_parts[index]
        if choose_part in computer_parts:
            print("Removing {}".format(choice))
            computer_parts.remove(choose_part)
        else:
            print("Adding {}".format(choice))
            computer_parts.append(choose_part)
        print("Now your list contain {}".format(computer_parts))
    else:
        print("select any option")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
    choice = input()
print("Your order will send soon to you door step {}".format(computer_parts))
