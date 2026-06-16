def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else:
        print("{} is not a number".format(temp))

value = get_integer(": ")

print("The value is {}".format(value))

#-------------------------------------------------

numbers = [4,8,9,2,4,7,3,1,5]
numbers.sort()
print(numbers)
