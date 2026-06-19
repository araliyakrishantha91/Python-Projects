def banner_text(text=" ",screen_width=80):
    if len(text) > screen_width - 4:
        # print("this text is too long ")
        raise ValueError("This text {0} is larger than the screen width {1}".format(text, screen_width))
    else:
        if text == "*":
            print("*"* screen_width)
        else:
            centered_text = text.center(screen_width -4)
            print("**{0}**".format(centered_text))

banner_text("*",66)
banner_text("Hi welcome to my home")
banner_text("you can take anything without my toys. love to see you",66)
banner_text("What is the your favourite song?")
banner_text()
banner_text("Cat and rat are good friends")
banner_text("Welcome back")
banner_text("Thank you!")
banner_text("*")
