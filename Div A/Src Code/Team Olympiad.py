n=int(input("Enter the number if childrens in the school: "))
t=[]
print("Enter the ti describes the skill of the i-th child: ")
for i in range(n):
    t.append(int(input()))
    
    
w=0 # for getting the largest possible numbers of teams: 
Teams=[]
for i in range(n):
    diff=0
    if t[i]!=0:
        internalTeams=[t[i]]
        for j in range(i+1,n):
            if t[j] in internalTeams or t[j]==0:
                continue
            internalTeams.append(t[j])
            t[j]=0
            diff+=1
            if diff==2:
                w+=1
                Teams.append(internalTeams)
                break
print(w)  
if w!=0:
    for i in range(w):
        for j in range(3):
             print(Teams[i][j],end=" ")    
        print()
        
    
            
            
    