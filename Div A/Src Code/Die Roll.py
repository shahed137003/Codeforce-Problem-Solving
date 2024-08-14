y=int(input("Enter the results of Yakko's die rolls: "))
w=int(input("Enter the results of Wakko's die rolls: "))
A=0
B=0
available=(6-max(y,w))+1
if available==6:
    A=1
    B=1
elif available==0:
    A=0
    B=1
elif available%2==0:
    A=int(available/2)
    B=3
elif available%3==0:
    A=int(available/3)
    B=2
    
else:
    A=available
    B=6

print(str(A)+"/"+str(B))
