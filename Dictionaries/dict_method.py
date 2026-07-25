d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four"
}

pantry_item = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)

k = d.keys()
print(k)
values = list(v)
keys = list(k)
print(values)
print(keys)
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was fount with the key {key}")

for key,value in d.items():
    if value == "four":
        print(f"{d[key]} was found with key {key}")


#print(values)
# for key,value in d.items():
#     print(key, value)


# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is the new three"
# }

# d.update(d2)
# for key,value in d.items():
#     print(key,value)
#
# print()
#
# d.update(enumerate(pantry_item))
# for key,value in sorted(d.items()):
#     print(key,value)
# new_dict = dict.fromkeys(pantry_item,0)
# print(pantry_item)
# print(new_dict)
#
# keys = d.keys()
# print(keys)
#
# for item in d.keys():
#     print(item)
