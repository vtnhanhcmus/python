# create empty tuple_tests
tuple_test = ()
print(tuple_test)

# one way create tuple_tests
tuple_test= "nhan", "vo"
print(tuple_test)

# another way create tuple_tests
tuple_test = ("nhan", "thanh", "vo")
print(tuple_test)

# add many tuple_tests together

tuple_test1 = (1,2,3,4,5)
tuple_test2 = "nhan", "vo", "thanh"

tuple_test = tuple_test1 + tuple_test2
#print(tuple_test)

# nesting of tuple_tests
tuple_test = (tuple_test1, tuple_test2)

#print(tuple_test)

# tuple_tests repetition

tuple_test = tuple_test1*3
#print(tuple_test)

# delete a tuple_tests
#del tuple_test
#print(tuple_test)

# slicing in tuple_tests

print(tuple_test1)

# print from 0 to 2
print(tuple_test1[:2])
# print from 1 to 3
print(tuple_test1[1:3])

# print reverse
print(tuple_test1[::-1])

# print len of tuple_tests
print(len(tuple_test))

# convert list to tuple_test
list_test = [1,2,4,6]
print(tuple(list_test))

# convert string to tuple
print(tuple("hello man"))






