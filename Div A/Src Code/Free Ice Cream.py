n=int(input("Enter the number of events : "))
x=int(input("Enter the number of existing ice cream backs: "))
d=[]
ch=[]
print("Enter the i-th place from the start of the queue: ")
for i in range(n):
    ch.append(input())
    d.append(int(input())) 
iceCreamBacks=x
distressedkids=0
for i in range(n):
    if ch[i]=='-':
        if iceCreamBacks>=d[i]:
            iceCreamBacks-=d[i]
        else:
            distressedkids+=1
    else:
        iceCreamBacks+=d[i]
        
            
print(str(iceCreamBacks)+" "+str(distressedkids))            