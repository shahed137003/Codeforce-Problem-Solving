n=int(input("Enter the number of cakes needed : "))
t=int(input("Enter the  time needed for one oven to bake k cakes: "))
k=int(input("Enter the  number of cakes baked at the same time: "))
d=int(input("Enter the time needed to bake the second oven: "))
totalTime=0
if n<=k:
    print("No")
else:
    totalTime=(n*t)/k
    if totalTime%d==0:
        print("No")
    else:
        print("Yes")
