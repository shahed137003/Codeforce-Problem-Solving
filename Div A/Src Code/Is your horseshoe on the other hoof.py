a=[]
print("Enter the colors of the horseshoes Valera has: ")
needed=0
for i in range(4):
    a.append(int(input()))
i=0
while i!=4:
    for j in range(i+1,4):
        if a[i]==a[j]:
            needed+=1
            i=j
    i+=1   
            
print(needed)