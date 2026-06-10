name = "araliya"
age = 26
print(name,age,"python",2026)
print(name,age,"python",2026, sep=", ")

menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "spam"],
    ["spam", "eggs", "bacon", "sausage"],
    ["spam", "bacon", "sausage", "spam"],
    ["eggs", "bacon", "sausage", "tomato", "spam"],
    ["eggs", "bacon", "spam", "tomato"]
]
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ") # default end is a new line
    print()
