a = set()
b = set()
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}

print(type(a))
print(type(b))


a.add(2)
print(a)

# add tuples in set
a.add((1,2))
print(a)

a.update([1,2])
print(a)

print(a.union(b))

# get common data between 2 arrays
print(a.intersection(b))


