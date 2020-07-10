lists = ['Mathematics', 'chemistry', 1997, 2000]
print(lists)

# append items
lists.append(456)
print(lists)

# insert item with index
lists.insert(1,3000)
print(lists)

# add content list1 to list
list1 = [1,2,3, 1]
lists.extend(list1)
print(lists)

# sum list
print(sum(list1))

# calculates total occurrence of given element of list.
print(lists.count(1))

# length of list
print(len(lists))

# min of list
print(min(list1))

# max of list
print(max(list1))


list3 = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

list3.sort(reverse=True)
print(list3)

list3.sort()
print(list3)

list3.pop()

print(list3)


list3.pop(0)
print(list3)

lists.remove(1997)
print(lists)

del lists[0]
print(lists)

