n=int(input("Enter the number of col in the box : "))
a=[]
print("Enter the number of cubes in the i-th column : ")

for i in range(n):
    a.append(int(input()))
    
    
#the case when we want to flip the box by the other direction : 

for i in range(n):
    for j in range(i,n):
        if a[i]>a[j]:
            diff=abs(a[i]-a[j])
            a[i]-=diff
            a[j]+=diff
            
        
        
for i in a:
    print(i ,end=" ")
    
