#functions 
#area of rectangle using functions
'''1.with argument without return type
2.with argument without no return type
3.without argument with return type
4.without argument withhout return type'''
#1
def rect(l,b):#l=length  b=breath
    l=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    r=l*b
    return r
a=10
b=20
result=rect(a,b)
print(result)


#2
def rect(l,b):#l=length  b=breath
    l=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    r=l*b
    print(r)
a=10
b=20
result=rect(a,b)


#3
def rect():#l=length  b=breath
    l=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    r=l*b
    print(r)
rect()


#4
  def rect():#l=length  b=breath
      l=int(input("enter the value of a"))
      b=int(input("enter the value of b"))
      r=l*b
      return r
  a=10
  b=20
  result=rect()
  print(result)
