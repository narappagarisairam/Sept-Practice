def fact(n):
    if n==0:
        return 1
    else:
        return n*fib(n-1)
n=int(input("enter the number")
result=fact(n)
print(result)
