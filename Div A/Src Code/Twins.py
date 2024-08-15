n=int(input("Enter the number of coins: "))
a=[]
print("Enter the values of each coin: ")
for i in range(n):
    a.append(int(input()))
    
for i in range(n):
    for j in range(i+1,n):
        if a[j]>a[i]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            
neededCoins=0
sumTotal=0

for i in range(n):
    remaining=0
    for j in range(i+1,n):
        remaining+=a[j]
    sumTotal+=a[i]
    neededCoins+=1
    if sumTotal>remaining:
        break
 
        
print(neededCoins)
