vehicles = {
    'black-boy':'pulsar 180',
    'fat-boy': 'hunk 150',
    'lean-boy': 'pulsar NS200',
    'legend': 'hornat 250',
    'loader': 'honda 125'
}

my_bike = vehicles['black-boy']
print(my_bike)
my_dream_bike = vehicles.get("legend")
print(my_dream_bike)
vehicles["blue-boy"] = "bajaj XCD125"
vehicles["lean-boy"] = "pulsar NS160"
print()
del vehicles["fat-boy"]
for key in vehicles:
    print(key, vehicles[key], sep=", ")

print()
result = vehicles.pop("lean-boy","wasn't present")
print(result)

for key, value in vehicles.items():
    print(key, value, sep=", ")
