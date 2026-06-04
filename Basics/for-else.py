numbers = [1,3,6,11,9]

for number in numbers:
    if number % 2 == 0:
        print("number {} is even".format(number))
        break
else:
    print("There is no any even number in numbers array")
