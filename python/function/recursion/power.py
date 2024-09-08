#power using recurstion function
def pow(n,m):
    if m==0:
        return 1
    else:
        return n**m 
n=int(input("enter the base"))
m=int(input("enter the power"))
result=pow(n,m)
print(result)
