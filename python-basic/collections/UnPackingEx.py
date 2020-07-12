# unpacking
a,b = (1, 2)
print(a)
print(b)

a,_ = (1,2)
print(a)

a,b,*c = [1,2,4,5,6,7,8]

print(a)
print(b)
print(c)



a,b,*_ = [1,2,4,5,6,7,8]

print(a)
print(b)



a,b,*c, d = [1,2,4,5,6,7,8]

print(a)
print(b)
print(c)
print(d)