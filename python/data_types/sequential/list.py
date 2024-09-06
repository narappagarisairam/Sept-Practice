#sequential_datatpe
#list
#append
a=[12,19,34,27,45,65,55,33]
a.append(98)
print(a)

#extend
a=[12,19,34,27,45,65,55,33]
a.extend([7,8])
print(a)

# insert it is used insert element where ever you want
a=[12,19,34,27,45,65,55,33]
a.insert(2,101)
print(a)

#remove
a=[12,19,34,27,45,65,55,33]
a.remove(33)
print(a)

#pop
a=[12,19,34,27,45,65,55,33]
a.pop()
print(a)

#clear
a=[12,19,34,27,45,65,55,33]
a.clear()
print(a)

#index
a=[12,19,34,27,45,65,55,33]
m=a.index(45)
print(m)

#count
a=[12,19,34,27,45,65,55,33,33]
i=a.count(33)
print(i)

#sort
a=[12,19,34,27,45,65,55,33]
a.sort()
print(a)

#reverse
a=[12,19,34,27,45,65,55,33]
a.reverse()
print(a)
