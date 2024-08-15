n=int(input("Enter the number of cities that exists in the lineland: "))
x=[]
for i in range(n):
    x.append(int(input()))
    
mindist=[]
maxdist=[]

for i in range(n):
    distances=[]
    for j in range(n):
        if j!=i:
            distances.append(abs(x[i]-x[j]))
    mindist.append(min(distances))
    maxdist.append(max(distances))
    
for i in range(n):
    print(str(mindist[i])+" "+str(maxdist[i]))