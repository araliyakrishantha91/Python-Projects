print("welcome to rollarcost")
height = int(input("what is your height? "))
bill = 0
if height >= 120:
    print("you can go rollarcost")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("child price is $5")
    elif age < 18:
        bill = 7
        print("teen price is $7")
    else:
        bill = 10
        print("adult price is $10")
    need_of_photo = input("do you need a photo? type y for YES and n for NO ")
    if need_of_photo == "y":
        bill += 3
    print(f"your bill is {bill}")
else:
    print("you have to be taller more than now")
