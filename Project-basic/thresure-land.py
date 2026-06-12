print(""""
                 _,__        .:
         Darwin <*  /        | \
            .-./     |.     :  :,
           /           '-._/     \_
          /                '       \
        .'                         *: Brisbane
     .-'                             ;
     |                               |
     \                              /
      |                            /
Perth  \*        __.--._          /
        \     _.'       \:.       |
        >__,-'             \_/*_.-'
                              Melbourne
                             :--,
                              '/
""")

print("welcome to treasure land game")
direction = input("left (l) or right (r) ? ").casefold()
if direction == "l":
    swim = input("swim (s) or wait (w) ? ").casefold()
    if swim == "w":
        door = input("which door green (g) red (r) or yellow (y) ?").casefold()
        if door == "y":
            print("you win !")
        else:
            print("game over !")
    else:
        print("game over !")
else:
    print("game over !")
