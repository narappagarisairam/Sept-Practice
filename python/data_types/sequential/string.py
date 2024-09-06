##string
#index forward
my_string = "Narappagari,sairam"
print(my_string[0])

#index backword
my_string = "Narappagari,sairam"
print(my_string[-1])

#slicing
my_string = "Narappagari,sairam"
print(my_string[1:4])

#length
my_string = "narappagari sairam"
print(len(my_string))

#upper_case
my_string = "narappagari sairam"
print(my_string.upper())

#lower_case
my_string = "narappagari sairam"
print(my_string.lower())

#strip
my_string = "   narappagari sairam"
print(my_string.strip())

#replace
my_string = "narappagari sairam"
print(my_string.replace("sairam", "Python"))

#split
my_string="narappagari sairam"
print(my_string.split())

#join method
words="narappagari sairam"
print(" ".join(words))

#join method
words="narappagari sairam"
print(" ".join(words))

#iindex method
my_string="narappagari sairam"
m=my_string.index('sairam')
print(m)

#count method
my_string="narappagari sairam"
my_string.count('a')

#start with
my_string="narappagari sairam"
my_string.startswith('ra')

# end with
my_string="narappagari sairam"
my_string.endswith('!')
