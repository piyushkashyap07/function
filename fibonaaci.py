def checkMember(n):
    x=0
    y=1
    if n==0 or n==1:
        return True
    z=0
    while z<=n+1:
        z=x+y
        x=y
        y=z
        if n==z:
            return True
    return False
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")