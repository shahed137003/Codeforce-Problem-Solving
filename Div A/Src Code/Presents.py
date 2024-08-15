n=int(input("Enter the number of fiend who will paricipate: "))
p=[]

print("Enter the i-th number is pi — the number of a friend who gave a gift to friend number i: ")
for i in range(n):
    p.append(int(input()))
    
l=[]

for i in range(n):
    for j in range(n):
        if p[j]==i+1:
            l.append(j+1)
            break
        
        
for i in range(n):
    print(l[i],end=" ")