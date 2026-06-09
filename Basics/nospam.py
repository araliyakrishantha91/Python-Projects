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
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#     else:
#         max_index = len(meal) - 1
#         for index,value in enumerate(reversed(meal)):
#             if value == "spam":
#                 del meal[max_index - index]
#         print(meal)

# for meal in menu:
#     for index in range (len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()
