width=0
friends=[]
n=int(input("please enter the number of friends:  "))
h=int(input("please enter the height of fence: "))

for i in range(n):
    friends.append(int(input(" ")))
    
    
for i in friends:
    if i<=h:
        width+=1
    else:
        width+=2


print("the minimum possible valid width of the road "+str(width))