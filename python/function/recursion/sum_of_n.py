#sum of n number using recursion number
def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1 
    else:
       return  n+sum(n-1)
result=sum(5)
print(result)
