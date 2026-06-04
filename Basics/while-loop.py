# for i in range(10):
#     print("i is now {}".format(i))
#
# i = 0
# while i<10:
#     print("i is now {}".format(i))
#     i += 1

options  = ["north" , "east" , "west" , "south"]
selection = ""


while selection not in options:
    selection = input("please select a option to exit: ")
    if selection.casefold() == "quit":
        print("Game Over")
        break
else:
    print("I'm glad about you")
