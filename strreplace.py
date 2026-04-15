age = 24
print("my age is " + str(age) + " years")
print("my age is {0} years" .format(age))
print("my name is {0}, and my age is {1}, my address is {2}, I have {3} sisters" .format("Amila",30,"Piliyandala",2))

for i in range(1, 13):
    print("No {0} squared is {1} and cubed is {2}" .format(i,i**2,i**3))
print()
for i in range(1, 13):
    print("No {0:2} squared is {1:3} and cubed is {2:4}" .format(i,i**2,i**3))
print()
for i in range(1, 13):
    print("No {0:2} squared is {1:<3} and cubed is {2:^4}" .format(i,i**2,i**3))
print()
print(f"Pi is approximately : {22/7:12.50f}")
print(f"Pi is approximately : {22/7:8.50f}")
pi = 22/7
print(f"Pi is approximately : {pi:72.54f}")
print(f"Pi is approximately : {pi:<72.54f}")
