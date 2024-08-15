n=int(input("Enter the number of electrical wires: "))
a=[] # the number of birdes in the electrical wire 
m=int(input("Enter the number of birdes to be shooted: "))
x=[]
y=[]
print("Enetr the number of birdes in each electrical wire: " )
for i in range(n):
    a.append(int(input()))
print("Enter  The integers mean that for the i-th time Shaass shoot the yi-th (from left) bird on the xi-th wire: ")
for i in range(m):
    x.append(int(input()))
    y.append(int(input()))
    
#################################################3
for i in range(m):
    if x[i]!=1 and x[i]!=n:
        
        a[x[i]]+=(a[x[i]-1]-y[i])
        a[x[i]-2]+=(y[i]-1)
        a[x[i]-1]=0
        
    elif x[i]==1:
         a[x[i]]+=(a[x[i]-1]-y[i])
         a[x[i]-1]=0
    else:
         a[x[i]-1]=0
         a[x[i]-2]+=(y[i]-1)
    
for i in range(n):
    print(a[i])
        
