choice = "_"
computer_parts = []
while choice != "0":
    if choice in "12345":
        print("selected {}".format(choice))
        computer_parts.append(choice)
    else:
        print("select any option")
        print("1.\tKeyboard")
        print("2.\tMouse")
        print("3.\tMonitor")
        print("4.\tCPU")
        print("5.\tMouse pad")
        print("0.\tExit")
    choice = input()
print(computer_parts)
