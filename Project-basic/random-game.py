import random
# import task
#
# random_integer = random.randint(1,10)
# print(random_integer)
# print(task.my_favourite_number)

# random_number_0_1 = random.random() * 10
# print(random_number_0_1)

# random_float = random.uniform(1,10)
# print(random_float)

# head_or_tail = random.randint(0,1)
# print(head_or_tail)
# if head_or_tail == 0:
#     print("Tail")
# else:
#     print("Head")
names = ["Bob", "Justin", "Suze", "Holdon", "Borgard"]
print(random.choice(names))

random_index = random.randint(0,4)
print(names[random_index])
