city = "Nuwara Eliya"
for letter in city:
    print(letter)

number = input("Please enter a number series with separators: ")
separator  = ""

for char in number:
    if not char.isnumeric():
        separator  = separator + char

print(separator)

for i in range(10, 16):
    print("i is now {}".format(i))
