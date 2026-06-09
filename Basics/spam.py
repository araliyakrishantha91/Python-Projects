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
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has {1} spams".format(meal, meal.count("spam")))
