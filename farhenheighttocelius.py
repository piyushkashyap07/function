def printTable(s,e,w):
    while (s<=e):
        c=((s-32)*5)/9
        print(s," ",int(c))
        s=s+w
    

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)



