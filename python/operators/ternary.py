#ternary operator
#to find max value

a = 10
b = 20

max_value = a if a > b else b #three conditions

print(max_value) 


# Finding the maximum of three numbers using nested ternary operators

a = 10
b = 20
c = 30

max_value = a if (a > b and a > c) else (b if b > c else c) #nested ternary operation

print(max_value)


#for function
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(check_even_odd(5))
print(check_even_odd(8))


# for lists
x = 5
my_list = [1, 2, 3] if x > 0 else [4, 5, 6]

print(my_list)

