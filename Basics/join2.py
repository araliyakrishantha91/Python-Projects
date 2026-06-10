animal = [
    "cat",
    "dog",
    "elephant",
    "horse",
    "tiger",
    "lion",
    "parrot",
    "donkey"
]
print(animal)
separator = " | "
output = separator.join(animal)
print(output)
print(animal)
print(" ".join(animal))
story = "All the soldiers go to war"
print(story)
split_story = (story.split())
print(split_story)
print(split_story[2])
numbers = "9,85,623,888,147,56,7"
split_numbers = numbers.split(",")
print(split_numbers)

for index in range(len(split_numbers)):
    split_numbers[index] = int(split_numbers[index])
print(split_numbers)

integer_values = []
for value in split_numbers:
    integer_values.append(int(value))
print(integer_values)
