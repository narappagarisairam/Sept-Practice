#identity operators
#is 
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # Output: True (values are equal)
print(a is b)  # Output: False (different memory locations)
print(a is c)  # Output: True (same memory location)



#is not
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)  # Output: True (a and b are different lists)
print(a == b)      # Output: True (but they have the same content)

