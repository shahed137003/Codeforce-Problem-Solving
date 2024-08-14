n=int(input("Enter the number of teams :"))
h=[]
a=[]

guestUniform=0

for i in range(n):
    h.append(int(input()))
    a.append(int(input()))

for i in range(n):
    for j in range(i+1,n):
        if a[i]==h[j]:
            guestUniform+=1
            

print(guestUniform)

