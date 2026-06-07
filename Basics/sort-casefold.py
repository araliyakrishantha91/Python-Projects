letters = sorted("Hi how are you guys", key = str.casefold)
print(letters)

test_list = ["nimal", "kasun", "amila", "Bandara", "bhanuka"]
test_list1 = sorted(test_list, key=str.casefold)
print(test_list1)

test_list.sort()
print(test_list)
test_list.sort(key=str.casefold)
print(test_list)
