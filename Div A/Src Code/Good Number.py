n=int(input("Enter the number n:"))
k=int(input("Enter the value of k: "))
a=[]
print("Enter the number in the array a: ")
for i in range(n):
    a.append(input())
    
k_good=0  
for i in range(n):
    notGuar=0
    for j in a[i]:
        num=int(j)
        if num>k:
            notGuar=1
    if notGuar==0:
        k_good+=1
        
            
            
print(k_good)