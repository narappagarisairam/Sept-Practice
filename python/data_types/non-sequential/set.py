#set operatons
#add
my_set = {1, 2, 3}
my_set.add(4) 
print(my_set)

#update
set={1,2,3}
set.update({4,5})
print(set)

#removing elements
set={1,2,3,4,5}
set.remove(3)
print(set)

#discard
my_set = {1, 2, 3}
my_set.discard(2)

#pop
my_set = {1, 2, 3}
removed_element = my_set.pop()  # removed_element might be 1, 2, or 3

#clear
my_set = {1, 2, 3}
my_set.clear()  # my_set becomes an empty set

#set mathmatical operation
#|,&,-,
my_set={1,2,3}
my_set1={4,5,6}
m=my_set|my_set1
print(m)

#and &
my_set={1,2,3,4}
my_set1={4,5,6}
m=my_set&my_set1
print(m)

#difference -
my_set={1,2,3,4}
my_set1={4,5,6}
m=my_set-my_set1
print(m)

#^
my_set={1,2,3,4}
my_set1={4,5,6}
m=my_set ^ my_set1
print(m)

#== elements should be same
set1 = {1, 2, 3,8}
set2 = {3, 2, 1,8}
print(set1 == set2)

#greater than
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1 <= set2)

#lesser than
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1 >= set2)

