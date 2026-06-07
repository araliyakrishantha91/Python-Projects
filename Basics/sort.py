even = [2,4,6,8]
odd = [1,3,5,7,9]

total = sum(even)
print(total)

even.extend(odd)
print(even)
another_even = even
print(another_even)
print(id(another_even))

even.sort()
print(even)
print(id(even))
even.sort(reverse=True)
print(id(even))
print(even)
print(another_even)
print(id(another_even))
print(id(even))
# every places id doesn't change. that means lists are mutable(can change). same variable is changed everywhere
