
import copy
# animals = {
#     "lion": "scary",
#     "elephant": "big",
#     "teddy": "cuddly"
# }
#
# #things = animals
# things = animals.copy()
# animals["teddy"] = "toy"
# print(things["teddy"])

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "gray", "huge"],
    "teddy": ["cuddly", "pretty"]
}
#things = animals.copy()
things = copy.deepcopy(animals)
things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
