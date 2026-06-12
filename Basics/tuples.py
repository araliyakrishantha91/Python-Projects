letters1 = ["a","b","c"]
letters2 = ("a","b","c")

print(type(letters1), type(letters2))
letters3 = list(letters2)
letters3[1] = "d"
print(letters3)

# Tuple unpacking
data = 1, 2, 76
x,y,z = data
print(x)
print(y)
print(z)

# list unpacking
data_list = [24, 36, 48]
a,b,c = data_list
print(a)
print(b)
print(c)
