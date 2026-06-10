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
    for index in range (len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))
