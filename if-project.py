name = input("Please enter your name ")
age = int(input("What is your age Mr.{0}? " .format(name)))
print("Mr.{0}'s age is {1}" .format(name,age))
#print(type(age))

if age>18:
    print("You have access")
else:
    if age==17:
        print("You have no access. Please wait {0} year" .format(18-age))
    elif age==18:
        print("Please give me your ID")
    else:
        print("You have no access. Please wait {0} years" .format(18-age))
