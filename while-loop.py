# for i in range(10):
#     print("i is now {}".format(i))
#
# i = 0
# while i<10:
#     print("i is now {}".format(i))
#     i += 1

options  = ["north" , "east" , "west" , "south"]
selection = ""
flag  = 0

while selection not in options:
    selection = input("please select a option to exit: ")
    if selection.casefold() == "quit":
        print("Game Over")
        flag = 1
        break
if flag == 0:
    print("I'm glad about you")
