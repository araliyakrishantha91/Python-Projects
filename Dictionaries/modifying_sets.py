numbers = set()

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value : "))
#     numbers.add(next_value)
# print(numbers)
data = ["blue","red","blue","green","red","blue","white"]
unique_data = sorted(set(data))
print(unique_data)

unique_data = list(dict.fromkeys(data))
print(unique_data)
