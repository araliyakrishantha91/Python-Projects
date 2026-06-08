data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# del data[0:2]
# print(data)
# del data[14:]
# print(data)
print(data)
min_value = 100
max_value = 200
stop = 0
for index,value in enumerate(data):
    if value >= min_value:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_value:
        start = index + 1
        break
print(start)
del data[start:]
print(data)
