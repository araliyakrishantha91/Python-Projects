print("welcome to online pizza ordering system")
bill = 0
size = input("what size pizza do you want, S M or L? ")
if size == "S".casefold():
    bill = 15
    print("small pizza price is $15")
elif size == "M".casefold():
    bill = 20
    print("medium pizza price is $20")
elif size == "L".casefold():
    bill = 25
    print("large pizza price is $25")
else:
    print("you entered a wrong input")
if size == "s".casefold() or size == "m".casefold() or size == "l".casefold():
    peparoni = input("do you need peparoni? y for YES n for NO ")
    if peparoni == "Y".casefold():
        if size == "S".casefold():
            bill += 2
        else:
            bill += 3

    cheese = input("do you need cheese? y for YES n for NO ")
    if cheese  == "Y".casefold():
        bill += 1

print(f"your total bill is ${bill}")
