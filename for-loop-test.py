city = "Nuwara Eliya"
for letter in city:
    print(letter)

number = input("Please enter a number series with separators: ")
separator  = ""

for char in number:
    if not char.isnumeric():
        separator  = separator + char

print(separator)

for i in range(20,10,-2):
    print("i is now {}".format(i))

age = int(input("enter your age: "))

if age in range(16,66):
    print("You can work")
else:
    print("don't do work")
