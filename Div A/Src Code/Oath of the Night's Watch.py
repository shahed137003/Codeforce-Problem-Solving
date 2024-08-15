n=int(input("Enter the number of stewards: "))
a=[]
print("Enter the strength of each ith steward: ")
for i in range(n):
    a.append(int(input()))
feeded=0
for i in range(n):
    greater=0
    smaller=0
    for j in range(n):
        if a[i]<a[j]:
            greater+=1
        elif a[i]>a[j]:
            smaller+=1        
    if greater>=1 and smaller>=1:
        feeded+=1
                      
print(feeded)               
                
            